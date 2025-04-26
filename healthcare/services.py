import requests
from django.conf import settings
from rest_framework.exceptions import APIException

class AsaasPaymentError(APIException):
    status_code = 400
    default_detail = 'Erro ao processar pagamento com Asaas'
    default_code = 'asaas_payment_error'

class AsaasService:
    BASE_URL = "https://www.asaas.com/api/v3"

    def __init__(self, api_key=None):
        self.api_key = api_key or settings.ASAAS_API_KEY

    def create_payment(self,amount, description, customer_id, split_items=None):
        # Mock implementation - in a real scenario, this would make an HTTP request
        if not self.api_key:
            raise AsaasPaymentError("Asaas API key not configured")
        
        # Simulate API call

        mock_response = {
            "id": "pay_123456789",
            "status": "PENDING",
            "invoiceUrl": "https://www.asaas.com/invoice/123456789",
            "split": split_items or []
        }

        return mock_response

    def split_payment(self, amount, professional_id, appointment_id):
        # Define split rules (70% to professional, 30% to platform)
        split_items = [
            {
                "walletId": settings.ASAAS_PROFESSIONAL_WALLET_ID,
                "fixedValue": round(amount * 0.7, 2),
                "description": f"Pagamento para profissional {professional_id}"
            },
            {
                "walletId": settings.ASAAS_PLATFORM_WALLET_ID,
                "fixedValue": round(amount * 0.3, 2),
                "description": "Taxa da plataforma"
            }
        ]

        return self.create_payment(
            amount=amount,
            description=f"Consulta {apointment_id}",
            customer_id="cust_123456"
            split_items=split_items
        )