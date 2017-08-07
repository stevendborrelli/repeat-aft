.. _roadmap:

Roadmap
=======

This document aims to give a high-level overview of where this project is
headed. The general next steps are:

 #. API specification and automated documentation:
    #. Automated, machine-readable documentation (Swagger?)
    #. Rigorous specification of valid responses (with JSON schema?)
    #. Rigorous specification of responses when errors are encountered
       (`Github issue #48 <https://github.com/ripeta/repeat-aft/issues/48>`_)
 #. Database improvements:
    #. Integrate with PostgreSQL as the primary database
    #. Periodically back up database (to S3 or similar cloud storage)
    #. Restore database upon boot
 #. Cloud storage for uploaded files
    (`Github issue #10 <https://github.com/ripeta/repeat-aft/issues/10>`_)
 #. Deployment to cloud providers
    (`Github issue #27 <https://github.com/ripeta/repeat-aft/issues/27>`_)
 #. Security:
    #. An integrated registration/authentication scheme
    #. Multiple levels of access
       (`Github issue #25 <https://github.com/ripeta/repeat-aft/issues/25>`_)
    #. Email confirmation for registration
       (`Github issue #26 <https://github.com/ripeta/repeat-aft/issues/26>`_)
    #. Throttling
       (`Github issue #47 <https://github.com/ripeta/repeat-aft/issues/47>`_)
