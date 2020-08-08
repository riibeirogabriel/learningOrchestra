# Projection microservice
Projection microservice provide an api to make a projection from file inserted in database service, generating a new file and putting in database

## POST IP:5001/projections/<filename>
```
{
    projection_filename : filename_to_save_projection,
    fields : [list, of, fields, to, be, used, in, projection]
}
```