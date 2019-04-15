# to run you need to locate this pcgi into cgi-bin folder
#!/usr/bin/env python3

import cgi;

# Useful debugging output
import cgitb
cgitb.enable()  # Send errors to browser
# cgitb.enable(display=0, logdir="/path/to/logdir") # log errors to a file

# Print the HTML MIME-TYPE header
print ("Content-Type: text/html\r\n\r\n")

# Now grab the content of the form
form = cgi.FieldStorage()

Gene_id    		= form["Gene identifier"].value
Products    	= form["Protein product names"].value
Accession		= form["GenBank Accession Number"].value
Locaton			= form["Chromosomal location"].value
query  = form.getlist("query")


html = "<html>\n"
html += "<head>\n"
html += "<title>Query results</title>\n"
html += "</head>\n\n"
html += "<body>\n"

# here begins the actul cgi
# REQUIREMENTS POINT 3: The detail page for a particular entry should allow you to view the following information:
# The complete DNA sequence with the coding regions highlighted
# The amino acid sequence displayed with the coding DNA sequence
# Codon usage frequencies within the coding region - the overall codon usage information for all sequences in the database should also be available (See the Notes page.)
# The ability to identify sticky-end restriction enzyme sites in the genomic DNA - i.e. in both coding and non-coding regions. Restriction enzymes that cut in the 5' upstream and/or 3' downstream regions, but not in-between should be highlighted. At a minimum you should include the ability to search for EcoRI, BamHI and BsuMI - optionally you may include other enzymes. You could also allow a restriction sequence to be entered by the user (see below).

html += "<h1>Query results</h1>\n"
html += "<h2>Your query was:</h2>\n"
html += "<pre>\n"

html += "<ul>"
for a in query:
    if a == "Gene_id":
        html += "<li>This Gene identifier corresponds to:</li>\n"
    if a == "Products":
        html += "<li>Protein product names correspond to</li>\n"
    if a == "Accession":
        html += "<li>GenBank accession number corresponds to</li>\n"
    if a == "Location":
        html += "<li>Chromosomal location corresponds to</li>\n"

html += "<h2>This corresponds to DNA sequence:</h2>"
# ...
html += "<h2>This corresponds to amino acid sequence:</h2>"
# ...
html += "<h2>Below the codon usage frequency table for this query:</h2>"
# ...
html += "<h2>Below sticky-end restriction enzyme sites in the genomic DNA corresponding to this query:</h2>"
#...

# I have been trying to work out how to display the results, but so far doesn't seem to work,
# here I left only stuff that will remain mostly unchanged, so you have the overview on how it's gonna work
# will have to adjust it again, but for now that's the overall structure that shouldn't change

html += "</ul>\n"
html += "</body>\n"
html += "</html>\n"

print (html)
