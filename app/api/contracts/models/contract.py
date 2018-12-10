from datetime import datetime

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
import uuid

from utils.entity import Entity


class ContractModel(Model):
    class Meta:
        table_name = "contract"
        read_capacity_units = 1
        write_capacity_units = 1
        host = 'http://localhost:8000'

    contract_id = UnicodeAttribute(hash_key=True)
    plan_id = UnicodeAttribute(null=False)
    license_key = UnicodeAttribute(null=True)
    customer_id = UnicodeAttribute(null=True)
    contract_type = UnicodeAttribute(null=False)
    contract_status = UnicodeAttribute(null=False)
    auto_renew_status = UnicodeAttribute(null=False)
    license_start_date = UTCDateTimeAttribute(null=True)
    license_end_date = UTCDateTimeAttribute(null=True)
    last_updated_vendor = UnicodeAttribute(null=False)
    contract_update_time = UTCDateTimeAttribute(null=True)
    contract_create_time = UTCDateTimeAttribute(null=True)

    def save(self, contract_id=None):
        if not contract_id:
            self.contract_id = str(uuid.uuid4())
        else:
            self.contract_id = contract_id
        now = datetime.utcnow()
        self.contract_create_time = now
        self.contract_update_time = now
        super().save()
        return self.contract_id

    def to_entity(self):
        return Entity.from_object({
            'contract_id': self.contract_id,
            'plan_id': self.plan_id,
            'license_key': self.license_key,
            'customer_id': self.customer_id,
            'contract_type': self.contract_type,
            'contract_status': self.contract_status,
            'auto_renew_status': self.auto_renew_status,
            'license_start_date': self.license_start_date.__str__(),
            'license_end_date': self.license_end_date.__str__(),
            'last_updated_vendor': self.last_updated_vendor
        })

    @classmethod
    def find_by_id(cls, contract_id):
        results = cls.query(contract_id)
        item = results.next()
        if item:
            return item
        return None
