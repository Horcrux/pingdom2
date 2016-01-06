# pingdom2
A Python utility to check if your website is up.

It will download a url and check for a text string on that page.
It emails you (and whoever else is in ```recipients```) when two consecutive checks fail.
It then shuts up for the duration of the downtime.
It sends one email when the site is back up.

Use in the form ```python3 pingdom2.py "http://url.to.check/foo/bar" "Text to check for on page"```

Best used with GNU ```screen``` to allow it to run in the background.

Logging is done in a textfile because stdout redirection is hard D:
