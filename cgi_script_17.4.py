#!/usr/bin/env python3

import cgi;

# Useful debugging output
import cgitb
cgitb.enable()
 
# Send errors to browser
# cgitb.enable(display=0, logdir="/path/to/logdir") 
# log errors to a file

# Print the HTML MIME-TYPE header
print ("Content-Type: text/html\r\n\r\n")

# Now grab the content of the form
form = cgi.FieldStorage()

Gene_id = form["gene_id"].value
Products = form["product_name"].value
Accession = form["accession_number"].value
Locaton = form["chr_location"].value


# changed "query" to "antype again to check whether misspelled () is to do with a novel name that shouldn't be used

html = "<html>"
html += "<head>\n"
html += "<title>Query results</title>\n"
html += "</head>\n\n"
html += "<body>\n"

# here begins the actual cgi
# REQUIREMENTS POINT 3: The detail page for a particular entry should allow you to view the following information:
# The complete DNA sequence with the coding regions highlighted
# The amino acid sequence displayed with the coding DNA sequence
# Codon usage frequencies within the coding region - the overall codon usage information for all sequences in the database should also be available (See the Notes page.)
# The ability to identify sticky-end restriction enzyme sites in the genomic DNA - i.e. in both coding and non-coding regions. Restriction enzymes that cut in the 5' upstream and/or 3' downstream regions, but not in-between should be highlighted. At a minimum you should include the ability to search for EcoRI, BamHI and BsuMI - optionally you may include other enzymes. You could also allow a restriction sequence to be entered by the user (see below).

html += "<h1>Query results</h1>\n"
html += "<h2>Your query was:</h2>\n"

### removed 4


### removed 3

html += "</body>\n"
html += "</html>\n"
print (html)