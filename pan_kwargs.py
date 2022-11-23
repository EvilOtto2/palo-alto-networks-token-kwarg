#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example Logging Service query using pancloud SDK."""

from pancloud import LoggingService, Credentials


# Base API URL
url = 'https://api.us.paloaltonetworks.com'

# Credentials
token = <your token>
c = Credentials(developer_token=token)

# Create Logging Service instance
ls = LoggingService(url=url, credentials=c)


query = {  # Prepare 'query' payload
    "query": "SELECT * FROM panw.traffic LIMIT 100",
    "startTime": 1552335543,
    "endTime": 1552335603,
    "maxWaitTime": 0  # no logs in initial response
}

# Create new 'query'
q = ls.query(query)

# Get 'queryId'
query_id = q.json()['queryId']

# Prepare 'poll' params
params = {
    "maxWaitTime": 3000
}

# Poll for results
p = ls.poll(query_id=query_id, sequence_no=0, params=params)

# Print results
print(p.text)
 @EvilOtto2
Write
