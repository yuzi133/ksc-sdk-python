# -*- encoding:utf-8 -*-
from kscore.session import get_session
import time
class KetClient:
	def __init__(self,service_name,region_name,use_ssl,ks_access_key_id,ks_secret_access_key):
		s = get_session()
		if ks_access_key_id != None and  ks_secret_access_key != None:
			self.client = s.create_client(service_name, region_name, use_ssl = use_ssl,
			ks_access_key_id=ks_access_key_id, ks_secret_access_key=ks_secret_access_key)
		else:
			self.client = s.create_client(service_name, region_name, use_ssl = use_ssl)

	def Preset(self,param):
		return self.client.preset(**param)

	def UpdatePreset(self,param):
		return self.client.update_preset(**param)

	def GetPresetList(self,App='live',UniqName=''):
		return self.client.get_preset_list(App=App,UniqName=UniqName)

	def GetPresetDetail(self,App='live',UniqName='',Preset=''):
		return self.client.get_preset_detail(App=App,UniqName=UniqName,Preset=Preset)

	def DelPreset(self,App='live',UniqName='',Preset=''):
		return self.client.del_preset(App=App,UniqName=UniqName,Preset=Preset)

	def StartStreamPull(self,param):
		return self.client.start_stream_pull(**param)

	def StopStreamPull(self,param):
		return self.client.stop_stream_pull(**param)

	def GetStreamTranList(self,App='live',UniqName='',StreamID='',OutPull=-1):
		return self.client.get_stream_tran_list(App=App,UniqName=UniqName,StreamID=StreamID,OutPull=OutPull)

	def GetQuotaUsed(self,UniqName=''):
		return self.client.get_quota_used(UniqName=UniqName)

def getKetClient(service_name,region_name,use_ssl=False,ks_access_key_id=None, ks_secret_access_key=None):
	return KetClient(service_name,region_name,use_ssl,ks_access_key_id,	ks_secret_access_key)
