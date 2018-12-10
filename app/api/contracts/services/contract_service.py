from datetime import datetime

from app.api.contracts.models.contract import ContractModel
import json

from utils.entity import Entity


def create_contract():
    ContractModel.create_table(wait=True)

    contract = ContractModel(
        plan_id='pid_1',
        customer_id='cid_1',
        contract_type='subscription',
        contract_status='inactive',
        auto_renew_status='none',
        last_updated_vendor='MS',
        license_start_date=datetime.utcnow(),
        license_end_date=datetime.utcnow()
    )
    contract_id = contract.save()
    return contract_id


def get_contract(contract_id):
    contract = ContractModel.find_by_id(contract_id)
    return contract.to_entity()

