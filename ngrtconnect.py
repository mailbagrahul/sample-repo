import saspy


class NGRT(object):
    def __init__(self, server):
        self.sas = saspy.SASsession(cfgname=server)

    def get_config(self, rev_path):
        self.sas.symput("revision_path", rev_path)
        self.confign = self.sas.submit(
            '''%include "/usr/apps/sasdata/ngrt/product_NGRT_sec/Local_Access/Prod_DropBox/RaaghulU/Get_config_name.sas";''')
        self.py_var = self.sas.symget("configname")
        print(self.py_var)
        return self.py_var

    def get_zo_data(self, rev_path):

        a = self.get_config(rev_path)
        return a


sas1 = NGRT('Product_NGRT_Sec')

config = sas1.get_zo_data('/usr/apps/sasdata/ngrt/product_NGRT_sec/Product_Sec/Revisions/VA/SAF_H6/HMR/20181018/RB/Iter_00_CRL')

print(config)
