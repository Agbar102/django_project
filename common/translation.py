from modeltranslation import translator
from common.models import *


@translator.register(Contacts)
class ContactsTranslations(translator.TranslationOptions):
    fields = ('company_name',)