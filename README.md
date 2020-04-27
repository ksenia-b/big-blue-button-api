
This API enables you to:
create meetings
join meetings
end meetings
get recordings for past meetings (and delete them)
upload closed caption files for meetings


checksum
This is basically a SHA-1 hash of
    callName + queryString + sharedSecret.
The security salt will be configured into the application at deploy time.
All calls to the API must include the checksum parameter.

to find those parameters use: bbb-conf --secret
