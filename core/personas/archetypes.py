from enum import Enum


class Archetype(str, Enum):
    POLITE = "polite"
    FRUSTRATED = "frustrated"
    CONFUSED = "confused"
    ADVERSARIAL = "adversarial"
    BILINGUAL = "bilingual"


class IssueType(str, Enum):
    SHIPPING_DELAY = "shipping_delay"
    WRONG_ITEM = "wrong_item"
    BILLING_ERROR = "billing_error"
    ACCOUNT_ACCESS = "account_access"
    PRODUCT_DEFECT = "product_defect"


class ResolutionExpectation(str, Enum):
    REFUND = "full_refund"
    REPLACEMENT = "replacement_item"
    EXPLANATION = "clear_explanation"
    APPOLOGY = "formal_apology"
    ACCOUNT_FIX = "account_restored"
