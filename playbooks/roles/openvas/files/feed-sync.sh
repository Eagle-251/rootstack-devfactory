#!/usr/bin/env bash
/usr/local/sbin/greenbone-feed-sync --type SCAP
sleep 2
/usr/local/sbin/greenbone-feed-sync --type CERT
sleep 2
/usr/local/sbin/greenbone-feed-sync --type GVMD_DATA
