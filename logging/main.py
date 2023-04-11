import logging

# Configuration from witch level want to log, default are: warning, error, critical
# logging.basicConfig(level=logging.DEBUG)
#
# # Save logs ot a file, appends logs to the end of the file
# logging.basicConfig(filename="my_logs.log", encoding="utf8")
#
# # Save logs to a file, but its overwritten each time filemode="w"
# logging.basicConfig(filename="my_logs2.log", encoding="utf8", filemode="w")
#
# # Interpolation:
# logging.info(f"The values is: {100}")
#
# # levels:
# logging.debug("Debug")
# logging.info("Info")
# logging.warning("Warning")
# logging.error("Error")
# logging.critical("Critical")


# Records attributes for detailed logs https://docs.python.org/3/library/logging.html#logrecord-attributes
# Must comment above configurations in order to work
logging.basicConfig(format="%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d [%(filename)s])",
                    datefmt="%d/%m/%Y %I:%M:%S %p",
                    level=logging.DEBUG)

logging.info("Hello my name is Slim Shady!")
logging.warning("Oh no! You caught me!")

import other_module

other_module.funct()
