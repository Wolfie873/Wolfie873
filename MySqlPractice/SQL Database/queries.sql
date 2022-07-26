-- Add a new column 'NewColumnName' to table 'TableName' in schema 'SchemaName'
ALTER TABLE SchemaName.users
    ADD id /*new_column_name*/ int /*new_column_datatype*/ NULL /*new_column_nullability*/ 
GO