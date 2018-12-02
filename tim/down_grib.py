#!/bin/python3

import datetime, subprocess

def main():

    # Wait 2 hours to ensure model is fully published
    utc = datetime.datetime.utcnow() - datetime.timedelta(hours=2)

    runTimes = [0, 6, 12, 18]

    for i in runTimes:
        if utc.hour > i:
            runHour = i;

    # Use current UTC to select URL for most up-to-date grib download
    baseURL = "http://www.ftp.ncep.noaa.gov/data/nccf/com/gfs/prod/"
    modelDir = "gfs.{:02d}{:02d}{:02d}{:02d}/".format(utc.year, utc.month, utc.day, runHour)
    gribDir = baseURL + modelDir

    gribTemplate = "gfs.t{:02d}z.pgrb2.0p25.f{:03d}"

    # Select paramaters of interests to extract from full grib file
    fieldTemplates = { 
            "UGRD" : ":UGRD:10 m above ground:{:d} hour fcst:",
            "VGRD" : ":VGRD:10 m above ground:{:d} hour fcst:",
            }

    # For each future hour and each field of interest download a file
    for i in range(1, 121):
        for j in fieldTemplates:

            gribFile = gribTemplate.format(runHour, i)
            indexFile = gribFile + ".idx"

            command = 'get_inv.pl "{:s}" | grep "{:s}" | get_grib.pl "{:s}" "{:s}"'.format(
                    gribDir + indexFile,
                    fieldTemplates[j].format(i),
                    gribDir + gribFile,
                    "{:s}.{:s}".format(gribFile, j)
                    )

            # Invoke bash sub-process to execute NOAA perl script to download
            subprocess.call(["bash", "-c", command])

main()
