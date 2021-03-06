from collections import OrderedDict
import numpy as np

'''
    5 loss combination strategies:
    - L1 > LT
    - L2 > LT
    - L1 + L2 > LT
    - L1 | L2 > LT
    - L1 & L2 > LT
    x ... jet_sample (pofah) or pandas data-frame (or rec-array)
'''

def combine_loss_l1(x):
    """ L1 > LT """
    return x['j1TotalLoss']

def combine_loss_l2(x):
    """ L2 > LT """
    return x['j2TotalLoss']

def combine_loss_sum(x):
    """ L1 + L2 > LT """
    return x['j1TotalLoss'] + x['j2TotalLoss']

def combine_loss_max(x):
    """ L1 | L2 > LT """
    return np.maximum(x['j1TotalLoss'], x['j2TotalLoss'])

def combine_loss_min(x):
    """ L1 & L2 > LT """
    return np.minimum(x['j1TotalLoss'], x['j2TotalLoss'])

def combine_loss_reco_min(x):
    """ Reco L1 & Reco L2 > LT """
    return np.minimum(x['j1RecoLoss'], x['j2RecoLoss'])

def combine_loss_kl1(x):
    ''' KL J1 '''
    return x['j1KlLoss']

def combine_loss_kl2(x):
    ''' KL J2 '''
    return x['j2KlLoss']

def combine_loss_kl_sum(x):
    ''' KL J1 + KL J2 '''
    return x['j1KlLoss'] + x['j2KlLoss']

def combine_loss_kl_max(x):
    ''' KL J1 | KL J2 '''
    return np.maximum(x['j1KlLoss'], x['j2KlLoss'])

def combine_loss_kl_min(x):
    ''' KL J1 & KL J2 '''
    return np.minimum(x['j1KlLoss'], x['j2KlLoss'])

def combine_loss_reco_kl_min(x):
    ''' (RecoLoss J1 + 10* KL J1) & (RecoLoss J2 + 10* KL J2) '''
    return np.minimum(x['j1RecoLoss']+10.*x['j1KlLoss'], x['j2RecoLoss']+10.*x['j2KlLoss']) 



class LossStrategy():

    def __init__(self, loss_fun, title_str, file_str):
        self.fun = loss_fun
        self.title_str = title_str
        self.file_str = file_str

    def __call__(self, x):
        return self.fun(x)


loss_strategy_dict = OrderedDict({ 
                     's1' : LossStrategy(combine_loss_l1, 'L1 > LT', 'l1_loss'),
                     's2': LossStrategy(combine_loss_l2, 'L2 > LT', 'l2_loss'),
                     's3': LossStrategy(combine_loss_sum, 'L1 + L2 > LT', 'suml1l2_loss'),
                     's4': LossStrategy(combine_loss_max, 'L1 | L2 > LT', 'maxl1l2_loss'),
                     's5': LossStrategy(combine_loss_min, 'L1 & L2 > LT', 'minl1l2_loss'),
                     'r5': LossStrategy(combine_loss_reco_min, 'R1 & R2 > LT', 'min_reco1reco2_loss'),
                     'kl1': LossStrategy(combine_loss_kl1, 'KL J1 > LT', 'kl1_loss'),
                     'kl2': LossStrategy(combine_loss_kl2, 'KL J2 > LT', 'kl2_loss'),
                     'kl3': LossStrategy(combine_loss_kl_sum, 'KL J1 + KL J2 > LT', 'sumKL_loss'),
                     'kl4': LossStrategy(combine_loss_kl_max, 'KL J1 | KL J2 > LT', 'maxKL_loss'),
                     'kl5': LossStrategy(combine_loss_kl_min, 'KL J1 & KL J2 > LT', 'minKL_loss'),
                     'rk5': LossStrategy(combine_loss_reco_kl_min, '(R J1 + 10* KL J1) & (R J2 + 10* KL J2)', 'min_recoKL_loss'), 
                 })
