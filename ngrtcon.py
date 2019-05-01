# -*- coding: utf-8 -*-
# @Author: N0207022
# @Date:   2019-04-03 12:02:22
# @Last Modified by:   n0207022
# @Last Modified time: 2019-04-23 22:48:31
import saspy

# from decorator_class import decoratorclass as decorate


class NGRT(object):

    # @decorate.my_log_time
    def __init__(self, server):
        print("Connecting to SAS")
        self.sas = "dsd"

    # @staticmethod
    # def error_finder(kickoff_log):
    #     log = kickoff_log['LOG']

    #     if "ERROR" in log:
    #         return True
    #     else:
    #         return False

    def get_config(self, rev_path):

        self.sas.submit(
            """%include "/usr/apps/sasdata/ngrt/product_NGRT_sec/Local_Access/Prod_DropBox/RaaghulU/Delete_Macro.sas";"""
        )

        self.sas.symput("revision_path", rev_path)
        test = " fdsf"
        self.py_var = self.sas.symget("revision_path")
        print("revision_path:" + self.py_var)

        self.confign = self.sas.submit(
            """%include "/usr/apps/sasdata/ngrt/product_NGRT_sec/Local_Access/Prod_DropBox/RaaghulU/Get_config_name.sas";"""
        )

        self.py_var = self.sas.symget("configname")
        print(self.sas.confign["LOG"])
        return self.py_var

    def kickoff(self, kick_prompts):

        self.sas.submit(
            """%include "/usr/apps/sasdata/ngrt/product_NGRT_sec/Local_Access/Prod_DropBox/RaaghulU/Delete_Macro.sas";"""
        )

        self.sas.symput("pmt_State", kick_prompts["state"])
        self.sas.symput("pmt_Brand", kick_prompts["brand"])
        self.sas.symput("pmt_LOB", kick_prompts["lob"])
        self.sas.symput("pmt_Prop_Date", kick_prompts["proposed_Date"])
        self.sas.symput("pmt_i_obs", kick_prompts["total_inf_records"])
        self.sas.symput("pmt_q_obs", kick_prompts["total_quote_records"])

        kickout = self.sas.submit(
            """%include "/usr/apps/sasdata/ngrt/product_NGRT_sec/Local_Access/Prod_DropBox/RaaghulU/UI/kick_off.sas";"""
        )

        # check for errors
        # error_ind = NGRT.error_finder(kickout)
        # if error_ind:
        #     return "Error"
        return "Folders created"

    def rater(self, config):

        self.sas.submit(
            """%include "/usr/apps/sasdata/ngrt/product_NGRT_sec/Local_Access/Prod_DropBox/RaaghulU/Delete_Macro.sas";"""
        )
        self.sas.symput("pmt_Browse_config", config)

        rater = self.sas.submit(
            """%include "/usr/apps/sasdata/ngrt/product_NGRT_sec/Local_Access/Prod_DropBox/RaaghulU/UI/rater_prod.sas";"""
        )

        # check for errors
        # error_ind = NGRT.error_finder(kickout)
        # if error_ind:
        #     return "Error"
        return "Rater ran successfully"

    # @decorate.my_log_time
    def get_files(self, path):
        return self.sas.dirlist(path)

    @property
    def saspid(self):
        return self.sas.SASpid

    def close_ngrt(self):
        self.sas._endsas()


# sas = NGRT('Product_NGRT_Sec')
