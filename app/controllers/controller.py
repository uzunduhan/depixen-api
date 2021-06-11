from google import auth as google_auth
from google.auth.transport import requests as google_auth_transport_requests
from google.auth.transport import grpc as google_auth_transport_grpc
from app.static.google.firestore.v1beta1 import firestore_pb2
from app.static.google.firestore.v1beta1 import firestore_pb2_grpc
from google.cloud import storage
from app.models import Urun
import os
import re

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../static/firebase-sdk.json'

scoped_credentials, _ = google_auth.default(scopes=('https://www.googleapis.com/auth/datastore',))
request = google_auth_transport_requests.Request()
channel = google_auth_transport_grpc.secure_authorized_channel(
scoped_credentials, request, 'firestore.googleapis.com:443')

stub = firestore_pb2_grpc.FirestoreStub(channel)

def UrunleriGetir():
    list_document_request = firestore_pb2.GetDocumentRequest(
    name = 'projects/depixen-project/databases/(default)/documents/urunlerim/urunAdlari')
    list_document_response = stub.GetDocument(list_document_request)

    list_document_response = list_document_response._fields

    list_document_response = list_document_response.__str__()
    urunler = re.findall('"(.*)"', list_document_response)
    return urunler

def UrununOzellikleriniGetir(urununAdi):
    urununAdi = str(urununAdi)
    if urununAdi!="secilmemis":
        urununAdi = urununAdi.replace(" ", "_")
        document_request = firestore_pb2.GetDocumentRequest(
        name = 'projects/depixen-project/databases/(default)/documents/urunler/{}'.format(urununAdi))
        document_response = stub.GetDocument(document_request)

        document_response = document_response.__str__()

        ozellikler = re.findall('"(.*)"', document_response)
        urununOzellikleri = Urun(ozellikler[4], ozellikler[8], ozellikler[2], ozellikler[10], ozellikler[6])

        return urununOzellikleri
