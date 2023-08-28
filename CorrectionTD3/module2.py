    #1.2 Arxiv
import urllib.request
    # the removal of links using the re module
import re
    # To parse the results using the xmltodict library, you can convert the XML response data into a Python dictionary using the xmltodict.parse() function. 
import xmltodict #need instal pip install xmltodict

    # Define the API query parameters
base_url = 'http://export.arxiv.org/api/query'
search_query = 'cat:cs.AI'
results_per_page = 10

    # Construct the API query URL
query_url = f'{base_url}?search_query={search_query}&max_results={results_per_page}'

    # Send an HTTP request to the API
response = urllib.request.urlopen(query_url)

    # Retrieve the response data
#data = response.read()

    # Print the response data
print("Print the response data: ")
#print(data)
print()

    # Retrieve the response data
data = response.read().decode('latin-1')

    # Remove links using regular expressions
data_without_links = re.sub(r'http\S+', '', data)

    # Print the data without links
print("Print the data without links: ")
print(data_without_links)
print()
    
    # Parser les r´esultat grˆace `a la libraire xmltodict.
    # Parse the XML response into a dictionary
parsed_data = xmltodict.parse(data)

    # Access the parsed data
entries = parsed_data['feed']['entry']

    # Print the titles of the entries
print("Print the titles of the entries: ")
for entry in entries:
    title = entry['title']
    print(title)
print()
    
    # Quels sont les champs disponibles ?
    # Get the keys of the parsed data dictionary
keys = parsed_data.keys()

    # Print the keys (fields) of the parsed data
print("Print the keys (fields) of the parsed data: ")
print(keys)
print()

    # Quel est le champ contenant le contenu textuel ?
    # Access the first result entry in the parsed data
first_entry = parsed_data['feed']['entry'][0]

    # Get the content text field
content_text = first_entry['summary']

    # Print the content text
print("Print the content text: ")
print(content_text)
print()

    #Alimentez la liste docs
    # Initialize the list to store the document texts
docs = []

    # Iterate over the entries in the parsed data
for entry in parsed_data['feed']['entry']:
    # Get the content text field
    content_text = entry['summary']
    
    # Append the content text to the docs list
    docs.append(content_text)
    
    # Print the populated docs list
print("Print the populated docs list: ")
print(docs)
