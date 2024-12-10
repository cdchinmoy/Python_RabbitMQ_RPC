
# Python_RabbitMQ_RPC

This project demonstrates an RPC (Remote Procedure Call) implementation using RabbitMQ and Python. It includes a Dockerized setup for ease of deployment and a client endpoint for generating PDFs.

---

## **Features**
- **RabbitMQ Integration**: Utilizes RabbitMQ for asynchronous communication.
- **PDF Generation**: Exposes an endpoint to create PDFs.
- **Docker Support**: Easy setup and deployment using Docker Compose.

---

## **Requirements**
- Docker
- Docker Compose

---

## **Setup and Run**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Python_RabbitMQ_RPC.git
   cd Python_RabbitMQ_RPC
   ```

2. **Build and Run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

3. The service will start with the following configurations:
   - **RabbitMQ** running in a container.
   - The **PDF generation service** exposed at `http://localhost:5000`.

---

## **Usage**

### **Client Endpoint**
The client endpoint for PDF creation is:

```
POST http://localhost:5000/create_pdf
```

#### Request Example:
Send a JSON payload:
```json
{
  "name": "Sample PDF",
  "email": "This is a test content for the PDF.",
  "phone": "8877665544",
  "address": "kushmandi"
}
```

#### Response Example:
```json
{
  "message": "PDF Generated!",
  "status": "Success"
}
```

---

## **Components**
- **RabbitMQ**: Used for RPC communication between the client and the worker service.
- **Worker Service**: Listens for requests and processes PDF creation tasks.
- **Client Service**: Exposes an API endpoint for initiating PDF creation requests.

---

## **Folder Structure**
```
Python_RabbitMQ_RPC/
├── docker-compose.yml       # Docker Compose configuration
├── client/                  # Client service code
├── worker/                  # Worker service code
├── rabbitmq/                # RabbitMQ configurations
└── README.md                # Project documentation
```

---

## **Contributing**
Feel free to fork this repository, open issues, and submit pull requests.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
