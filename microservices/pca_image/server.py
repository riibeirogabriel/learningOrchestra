from flask import jsonify, request, Flask, send_file
import os
from pca import Pca
from utils import Database, UserRequest
from concurrent.futures import ThreadPoolExecutor

HTTP_STATUS_CODE_SUCCESS = 200
HTTP_STATUS_CODE_SUCCESS_CREATED = 201
HTTP_STATUS_CODE_CONFLICT = 409
HTTP_STATUS_CODE_NOT_ACCEPTABLE = 406
HTTP_STATUS_CODE_NOT_FOUND = 404

PCA_HOST_IP = "PCA_HOST_IP"
PCA_HOST_PORT = "PCA_HOST_PORT"

IMAGES_PATH = "IMAGES_PATH"
IMAGE_FORMAT = ".png"

DATABASE_URL = "DATABASE_URL"
DATABASE_PORT = "DATABASE_PORT"
DATABASE_NAME = "DATABASE_NAME"
DATABASE_REPLICA_SET = "DATABASE_REPLICA_SET"

MESSAGE_RESULT = "result"
PCA_FILENAME_NAME = "outputPlotName"
PARENT_FILENAME_NAME = "inputDatasetName"
LABEL_NAME = "label"

MESSAGE_DELETED_FILE = "deleted file"

FIRST_ARGUMENT = 0

MICROSERVICE_URI_GET = "/api/learningOrchestra/v1/explore/pca/"

app = Flask(__name__)

thread_pool = ThreadPoolExecutor()


@app.route("/images", methods=["POST"])
def pca_plot():
    database = Database(
        os.environ[DATABASE_URL],
        os.environ[DATABASE_REPLICA_SET],
        os.environ[DATABASE_PORT],
        os.environ[DATABASE_NAME]
    )
    request_validator = UserRequest(database)

    request_errors = analyse_request_errors(
        request_validator,
        request.json[PARENT_FILENAME_NAME],
        request.json[PCA_FILENAME_NAME],
        request.json[LABEL_NAME])

    if request_errors is not None:
        return request_errors

    database_url_input = Database.collection_database_url(
        os.environ[DATABASE_URL],
        os.environ[DATABASE_NAME],
        request.json[PARENT_FILENAME_NAME],
        os.environ[DATABASE_REPLICA_SET],
    )

    thread_pool.submit(pca_async_processing,
                       database_url_input,
                       request.json[LABEL_NAME],
                       request.json[PCA_FILENAME_NAME])

    return (
        jsonify({
            MESSAGE_RESULT:
                MICROSERVICE_URI_GET +
                request.json[PCA_FILENAME_NAME]}),
        HTTP_STATUS_CODE_SUCCESS_CREATED,
    )


@app.route("/images", methods=["GET"])
def get_images():
    images = os.listdir(os.environ[IMAGES_PATH])
    return jsonify({MESSAGE_RESULT: images}), HTTP_STATUS_CODE_SUCCESS


@app.route("/images/<filename>", methods=["GET"])
def get_image(filename):
    try:
        UserRequest.pca_filename_nonexistence_validator(filename)

    except Exception as invalid_pca_filename:
        return (
            jsonify(
                {MESSAGE_RESULT: invalid_pca_filename.args[FIRST_ARGUMENT]}),
            HTTP_STATUS_CODE_NOT_FOUND,
        )

    image_path = os.environ[IMAGES_PATH] + "/" + filename + IMAGE_FORMAT

    return send_file(image_path, mimetype="image/png")


@app.route("/images/<filename>", methods=["DELETE"])
def delete_image(filename):
    try:
        UserRequest.pca_filename_nonexistence_validator(filename)
    except Exception as invalid_pca_filename:
        return (
            jsonify(
                {MESSAGE_RESULT: invalid_pca_filename.args[FIRST_ARGUMENT]}),
            HTTP_STATUS_CODE_NOT_FOUND,
        )

    image_path = os.environ[IMAGES_PATH] + "/" + filename + IMAGE_FORMAT

    thread_pool.submit(os.remove, image_path)

    return jsonify(
        {MESSAGE_RESULT: MESSAGE_DELETED_FILE}), HTTP_STATUS_CODE_SUCCESS


def pca_async_processing(database_url_input, label_name,
                         pca_filename):
    pca_generator = Pca(database_url_input)

    pca_generator.create_image(
        label_name, pca_filename
    )


def analyse_request_errors(request_validator, parent_filename,
                           pca_filename, label_name):
    try:
        request_validator.pca_filename_existence_validator(
            pca_filename
        )
    except Exception as invalid_pca_filename:
        return (
            jsonify(
                {MESSAGE_RESULT: invalid_pca_filename.args[FIRST_ARGUMENT]}),
            HTTP_STATUS_CODE_CONFLICT,
        )

    try:
        request_validator.parent_filename_validator(
            parent_filename)
    except Exception as invalid_filename:
        return (
            jsonify({MESSAGE_RESULT: invalid_filename.args[FIRST_ARGUMENT]}),
            HTTP_STATUS_CODE_NOT_ACCEPTABLE,
        )

    try:
        request_validator.filename_label_validator(
            parent_filename, label_name
        )
    except Exception as invalid_label:
        return (
            jsonify({MESSAGE_RESULT: invalid_label.args[FIRST_ARGUMENT]}),
            HTTP_STATUS_CODE_NOT_ACCEPTABLE,
        )

    try:
        request_validator.finished_processing_validator(
            parent_filename)
    except Exception as unfinished_filename:
        return jsonify(
            {MESSAGE_RESULT: unfinished_filename.args[FIRST_ARGUMENT]}), \
               HTTP_STATUS_CODE_NOT_ACCEPTABLE

    return None


if __name__ == "__main__":
    app.run(host=os.environ[PCA_HOST_IP], port=int(os.environ[PCA_HOST_PORT]))
