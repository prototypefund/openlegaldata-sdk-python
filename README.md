# oldp-api
With the Open Legal Data API you can access various data from the legal domain, e.g. law text or case files. The data may be used for semantic analysis or to create statistics. For more information visit our website.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 0.1.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/openlegaldata/oldp-sdk-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/openlegaldata/oldp-sdk-python.git`)

Then import the package:
```python
import oldp_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import oldp_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import oldp_client
from oldp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
oldp_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# oldp_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
# create an instance of the API class
api_instance = oldp_client.AnnotationLabelsApi()
data = oldp_client.AnnotationLabel() # AnnotationLabel | 

try:
    api_response = api_instance.annotation_labels_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationLabelsApi->annotation_labels_create: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://de.openlegaldata.io/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnnotationLabelsApi* | [**annotation_labels_create**](docs/AnnotationLabelsApi.md#annotation_labels_create) | **POST** /annotation_labels/ | 
*AnnotationLabelsApi* | [**annotation_labels_delete**](docs/AnnotationLabelsApi.md#annotation_labels_delete) | **DELETE** /annotation_labels/{id}/ | 
*AnnotationLabelsApi* | [**annotation_labels_list**](docs/AnnotationLabelsApi.md#annotation_labels_list) | **GET** /annotation_labels/ | 
*AnnotationLabelsApi* | [**annotation_labels_partial_update**](docs/AnnotationLabelsApi.md#annotation_labels_partial_update) | **PATCH** /annotation_labels/{id}/ | 
*AnnotationLabelsApi* | [**annotation_labels_read**](docs/AnnotationLabelsApi.md#annotation_labels_read) | **GET** /annotation_labels/{id}/ | 
*AnnotationLabelsApi* | [**annotation_labels_update**](docs/AnnotationLabelsApi.md#annotation_labels_update) | **PUT** /annotation_labels/{id}/ | 
*CaseAnnotationsApi* | [**case_annotations_create**](docs/CaseAnnotationsApi.md#case_annotations_create) | **POST** /case_annotations/ | 
*CaseAnnotationsApi* | [**case_annotations_delete**](docs/CaseAnnotationsApi.md#case_annotations_delete) | **DELETE** /case_annotations/{id}/ | 
*CaseAnnotationsApi* | [**case_annotations_list**](docs/CaseAnnotationsApi.md#case_annotations_list) | **GET** /case_annotations/ | 
*CaseAnnotationsApi* | [**case_annotations_partial_update**](docs/CaseAnnotationsApi.md#case_annotations_partial_update) | **PATCH** /case_annotations/{id}/ | 
*CaseAnnotationsApi* | [**case_annotations_read**](docs/CaseAnnotationsApi.md#case_annotations_read) | **GET** /case_annotations/{id}/ | 
*CaseAnnotationsApi* | [**case_annotations_update**](docs/CaseAnnotationsApi.md#case_annotations_update) | **PUT** /case_annotations/{id}/ | 
*CasesApi* | [**cases_create**](docs/CasesApi.md#cases_create) | **POST** /cases/ | 
*CasesApi* | [**cases_delete**](docs/CasesApi.md#cases_delete) | **DELETE** /cases/{id}/ | 
*CasesApi* | [**cases_list**](docs/CasesApi.md#cases_list) | **GET** /cases/ | 
*CasesApi* | [**cases_partial_update**](docs/CasesApi.md#cases_partial_update) | **PATCH** /cases/{id}/ | 
*CasesApi* | [**cases_read**](docs/CasesApi.md#cases_read) | **GET** /cases/{id}/ | 
*CasesApi* | [**cases_search_list**](docs/CasesApi.md#cases_search_list) | **GET** /cases/search/ | 
*CasesApi* | [**cases_search_read**](docs/CasesApi.md#cases_search_read) | **GET** /cases/search/{id}/ | 
*CasesApi* | [**cases_update**](docs/CasesApi.md#cases_update) | **PUT** /cases/{id}/ | 
*CitiesApi* | [**cities_list**](docs/CitiesApi.md#cities_list) | **GET** /cities/ | 
*CitiesApi* | [**cities_read**](docs/CitiesApi.md#cities_read) | **GET** /cities/{id}/ | 
*CountriesApi* | [**countries_list**](docs/CountriesApi.md#countries_list) | **GET** /countries/ | 
*CountriesApi* | [**countries_read**](docs/CountriesApi.md#countries_read) | **GET** /countries/{id}/ | 
*CourtsApi* | [**courts_list**](docs/CourtsApi.md#courts_list) | **GET** /courts/ | 
*CourtsApi* | [**courts_read**](docs/CourtsApi.md#courts_read) | **GET** /courts/{id}/ | 
*LawBooksApi* | [**law_books_create**](docs/LawBooksApi.md#law_books_create) | **POST** /law_books/ | 
*LawBooksApi* | [**law_books_delete**](docs/LawBooksApi.md#law_books_delete) | **DELETE** /law_books/{id}/ | 
*LawBooksApi* | [**law_books_list**](docs/LawBooksApi.md#law_books_list) | **GET** /law_books/ | 
*LawBooksApi* | [**law_books_partial_update**](docs/LawBooksApi.md#law_books_partial_update) | **PATCH** /law_books/{id}/ | 
*LawBooksApi* | [**law_books_read**](docs/LawBooksApi.md#law_books_read) | **GET** /law_books/{id}/ | 
*LawBooksApi* | [**law_books_update**](docs/LawBooksApi.md#law_books_update) | **PUT** /law_books/{id}/ | 
*LawsApi* | [**laws_create**](docs/LawsApi.md#laws_create) | **POST** /laws/ | 
*LawsApi* | [**laws_delete**](docs/LawsApi.md#laws_delete) | **DELETE** /laws/{id}/ | 
*LawsApi* | [**laws_list**](docs/LawsApi.md#laws_list) | **GET** /laws/ | 
*LawsApi* | [**laws_partial_update**](docs/LawsApi.md#laws_partial_update) | **PATCH** /laws/{id}/ | 
*LawsApi* | [**laws_read**](docs/LawsApi.md#laws_read) | **GET** /laws/{id}/ | 
*LawsApi* | [**laws_search_list**](docs/LawsApi.md#laws_search_list) | **GET** /laws/search/ | 
*LawsApi* | [**laws_search_read**](docs/LawsApi.md#laws_search_read) | **GET** /laws/search/{id}/ | 
*LawsApi* | [**laws_update**](docs/LawsApi.md#laws_update) | **PUT** /laws/{id}/ | 
*StatesApi* | [**states_list**](docs/StatesApi.md#states_list) | **GET** /states/ | 
*StatesApi* | [**states_read**](docs/StatesApi.md#states_read) | **GET** /states/{id}/ | 
*TokenAuthApi* | [**token_auth_create**](docs/TokenAuthApi.md#token_auth_create) | **POST** /token-auth/ | 
*UsersApi* | [**users_list**](docs/UsersApi.md#users_list) | **GET** /users/ | 
*UsersApi* | [**users_me**](docs/UsersApi.md#users_me) | **GET** /users/me/ | 
*UsersApi* | [**users_read**](docs/UsersApi.md#users_read) | **GET** /users/{id}/ | 


## Documentation For Models

 - [AnnotationLabel](docs/AnnotationLabel.md)
 - [Case](docs/Case.md)
 - [CaseAnnotation](docs/CaseAnnotation.md)
 - [CaseSearch](docs/CaseSearch.md)
 - [City](docs/City.md)
 - [Country](docs/Country.md)
 - [Court](docs/Court.md)
 - [CourtMinimal](docs/CourtMinimal.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [Law](docs/Law.md)
 - [LawBook](docs/LawBook.md)
 - [LawSearch](docs/LawSearch.md)
 - [State](docs/State.md)
 - [User](docs/User.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

hello@openlegaldata.io

