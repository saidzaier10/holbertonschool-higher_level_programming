#!/user/bin/python3

import os
import logging


def generate_invitations(template, attendees):
    # Set up logging
    logging.basicConfig(level=logging.ERROR)
    logger = logging.getLogger(__name__)

    # Check if template is a string
    if not isinstance(template, str):
        logger.error("Invalid input: template is not a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        logger.error("Invalid input: attendees is not a list of dictionaries.")
        return

    # Check if template is empty
    if not template:
        logger.error("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        logger.error("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        try:
            # Replace placeholders with actual values or "N/A" if missing
            filled_template = template.format(
                name=attendee.get("name", "N/A"),
                event_title=attendee.get("event_title", "N/A"),
                event_date=attendee.get("event_date", "N/A"),
                event_location=attendee.get("event_location", "N/A"),
            )

            # Generate output file
            output_filename = f"output_{index}.txt"
            if os.path.exists(output_filename):
                logger.error(f"File {output_filename} already exists.")
            else:
                with open(output_filename, "w") as file:
                    file.write(filled_template)
        except Exception as e:
            logger.error(f"Error processing attendee {index}: {e}")
            # Call the function with the template and attendees list
            generate_invitations(template, attendees)
