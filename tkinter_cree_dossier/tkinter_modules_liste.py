from tkinter_cree_dossier.tkinter_mdl import Module_Mdl

from tkinter_cree_dossier.tkinter_insts import i_Activation
from tkinter_cree_dossier.tkinter_insts import i_Biais
from tkinter_cree_dossier.tkinter_insts import i_Kconvl2d_stricte
from tkinter_cree_dossier.tkinter_insts import i_MatMul, i_MatMul_Canal
from tkinter_cree_dossier.tkinter_insts import i_Mul2, i_Mul3
from tkinter_cree_dossier.tkinter_insts import i_Pool2x2
from tkinter_cree_dossier.tkinter_insts import i_Softmax
from tkinter_cree_dossier.tkinter_insts import i_Somme2, i_Somme3, i_Somme4

conn = lambda sortie,inst,entree: (sortie, (inst,entree))

class DOT1D(Module_Mdl):	#	f(ax+b)
	nom = "DOT1D : f(AX+B)"
	X, Y = [0], [0]
	X_noms, Y_noms = ["X"], ["Y"] # LSTM [X], [H]
	params = {
		'activ' : 0
	}
	def cree_ix(self):
		#	Params
		activ = self.params['activ']
		X = self.X[0]
		Y = self.Y[0]

		#	------------------

		self.ix = [
			 ax :={'i':i_MatMul    , 'X':[X  ],'x':[None], 'xt':[None], 'y':Y, 'p':[     ], 'sortie':False, '0':0},
			   b:={'i':i_Biais     , 'X':[   ],'x':[    ], 'xt':[    ], 'y':Y, 'p':[     ], 'sortie':False, '1':1},
			 axb:={'i':i_Somme2    , 'X':[Y,Y],'x':[ax,b], 'xt':[0,0 ], 'y':Y, 'p':[     ], 'sortie':False, '2':2},
			faxb:={'i':i_Activation, 'X':[Y  ],'x':[axb ], 'xt':[  0 ], 'y':Y, 'p':[activ], 'sortie':True , '3':3}
		]

		for i in range(len(self.ix)):
			assert self.ix[i][str(i)] == i

	def module_vers_model(self):
		self.cree_ix()
		self.insts_et_connections(ix)

class DOT1D_2(Module_Mdl):	#	f(ax0+bx1+c)
	nom = "DOT1D_2 : f(AX0+BX1+C)"
	X, Y = [0,0], [0]
	X_noms, Y_noms = ["X0","X1"], ["Y"] # LSTM [X], [H]
	params = {
		'activ' : 0
	}
	def cree_ix(self):
		#	Params
		activ = self.params['activ']
		X0 = self.X[0]
		X1 = self.X[1]
		Y  = self.Y[0]

		#	------------------

		self.ix = [
			  ax0:={'i':i_MatMul    , 'X':[X0 ],'x':[None], 'xt':[None], 'y':Y, 'p':[     ], 'sortie':False, '0':0},
			  bx1:={'i':i_MatMul    , 'X':[X1 ],'x':[None], 'xt':[None], 'y':Y, 'p':[     ], 'sortie':False, '1':1},
			    c:={'i':i_Biais     , 'X':[   ],'x':[    ], 'xt':[    ], 'y':Y, 'p':[     ], 'sortie':False, '2':2},

			axbxc:={'i':i_Somme3    , 'X':[Y,Y,Y],'x':[ax0,bx1,c], 'xt':[0,0,0], 'y':Y, 'p':[     ], 'sortie':False, '3':3},
			 faxb:={'i':i_Activation, 'X':[Y    ],'x':[axbxc ], 'xt':[  0 ], 'y':Y, 'p':[activ], 'sortie':True , '4':4}
		]

		for i in range(len(self.ix)):
			assert self.ix[i][str(i)] == i

	def module_vers_model(self):
		self.cree_ix()
		self.insts_et_connections(ix)

class DOT1D_3(Module_Mdl):	#	f(ax0+bx1+cx2+d)
	nom = "DOT1D_3 : f(AX0+BX1+CX2+D)"
	X, Y = [0,0,0], [0]
	X_noms, Y_noms = ["X0","X1","X2"], ["Y"] # LSTM [X], [H]
	params = {
		'activ' : 0
	}
	def cree_ix(self):
		#	Params
		activ = self.params['activ']
		X0 = self.X[0]
		X1 = self.X[1]
		X2 = self.X[2]
		Y  = self.Y[0]

		#	------------------

		self.ix = [
			ax0:={'i':i_MatMul    , 'X':[X0 ],'x':[None], 'xt':[None], 'y':Y, 'p':[     ], 'sortie':False, '0':0},
			bx1:={'i':i_MatMul    , 'X':[X1 ],'x':[None], 'xt':[None], 'y':Y, 'p':[     ], 'sortie':False, '1':1},
			cx2:={'i':i_MatMul    , 'X':[X2 ],'x':[None], 'xt':[None], 'y':Y, 'p':[     ], 'sortie':False, '2':2},
			  d:={'i':i_Biais     , 'X':[   ],'x':[    ], 'xt':[    ], 'y':Y, 'p':[     ], 'sortie':False, '3':3},

			axbxcxd:={'i':i_Somme4,  'X':[Y,Y,Y,Y],'x':[ax0,bx1,cx2,d], 'xt':[0,0,0,0], 'y':Y, 'p':[     ], 'sortie':False, '4':4},
			faxb:={'i':i_Activation, 'X':[Y],'x':[axbxc ], 'xt':[  0 ], 'y':Y, 'p':[activ], 'sortie':True , '5':5}
		]

		for i in range(len(self.ix)):
			assert self.ix[i][str(i)] == i

	def module_vers_model(self):
		self.cree_ix()
		self.insts_et_connections(ix)

#	======================================================================

class LSTM1D(Module_Mdl):	#	f(ax0+bx1+cx2+d)
	nom = "LSTM 1D"
	X, Y = [0], [0]
	X_noms, Y_noms = ["X"], ["H"] # LSTM [X], [H]
	params = {
		#'activ' : 0
	}
	def cree_ix(self):
		#	Params
		activ = self.params['activ']
		X = self.X[0]
		Y = self.Y[0]

		#	------------------

		_tanh      = 0
		logistique = 1

		h = "ref a h"
		c = "ref a c"

		self.ix = [
		# f = logistique(sF = Fx@x + Fh@h + Fc@c[-1] + Fb)
		# i = logistique(sI = Ix@x + Ih@h + Ic@c[-1] + Ib)
		#u =       tanh(sU = Ux@x + Uh@h +          + Ub)
		#c = f*c[-1] + i*u

		#ch = tanh(c)

		#o = logistique(sO = Ox@x + Oh@h + Oc@c    + Ob)

		
		#h = o * ch
		]

		#for l in self.ix:
		#	if h alors 'x', 'xt' = h
		#	if c alors 'x', 'xt' = c

		for i in range(len(self.ix)):
			assert self.ix[i][str(i)] == i

	def module_vers_model(self):
		self.cree_ix()
		self.insts_et_connections(ix)

modules = [DOT1D, DOT1D_2, DOT1D_3]