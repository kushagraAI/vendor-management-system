INITIAL SETUP

Clone the repository:
git clone https://github.com/kushagraAI/Vendor-management-system.git

Navigate to the project directory:
cd Vendor-management-system

Activate virtualenv
venv\scripts\activate


Install dependencies:
pip install -r requirements.txt


Apply database migrations:
python manage.py migrate


Run the development server using following command:
python manage.py runserver


API Endpoint Details:


VENDORS:

1. List/Create Vendors:

URL: api/vendors/
Method: GET (List Vendors), POST (Create Vendor)
Authentication: Token Authentication required

2. Retrieve/Update Vendor:

URL: api/vendors/<int:pk>/
Method: GET (Retrieve Vendor), PUT (Update Vendor)
Authentication: Token Authentication required

3. Delete Vendor:

URL: api/vendors/delete/<int:pk>/
Method: DELETE
Authentication: Token Authentication required

PURCHASE ORDERS:

1. List/Create Purchase Orders:

URL: api/purchase-orders/
Method: GET (List Purchase Orders), POST (Create Purchase Order)
Authentication: Token Authentication required

2. Retrieve/Update Purchase Order:

URL: api/purchase-orders/<int:pk>/
Method: GET (Retrieve Purchase Order), PUT (Update Purchase Order)
Authentication: Token Authentication required

3. Delete Purchase Order:

URL: api/purchase-orders/delete/<int:pk>/
Method: DELETE
Authentication: Token Authentication required.

--------------------------------------------

Acknowledge Purchase Order:

URL: api/purchase-orders/<int:pk>/acknowledge/
Method: PUT (Acknowledge Purchase Order)
Authentication: Token Authentication required


Retrieve Vendor Performance:

URL: /vendors/<int:pk>/performance/
Method: GET (Retrieve Vendor Performance)
Authentication: Token Authentication required


