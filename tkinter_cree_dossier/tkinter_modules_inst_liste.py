from tkinter_cree_dossier.tkinter_mdl import Module_Mdl
from tkinter_cree_dossier.tkinter_insts import liste_insts

from tkinter_cree_dossier.tkinter_insts import i__Entree
from tkinter_cree_dossier.tkinter_insts import i_Activation
from tkinter_cree_dossier.tkinter_insts import i_Biais
from tkinter_cree_dossier.tkinter_insts import i_Kconvl2d_stricte
from tkinter_cree_dossier.tkinter_insts import i_MatMul, i_MatMul_Canal
from tkinter_cree_dossier.tkinter_insts import i_Mul2, i_Mul3
from tkinter_cree_dossier.tkinter_insts import i_Pool2x2
from tkinter_cree_dossier.tkinter_insts import i_Softmax
from tkinter_cree_dossier.tkinter_insts import i_Somme2, i_Somme3, i_Somme4

conn = lambda sortie,inst,entree: (sortie, (inst,entree))

modules_inst = []

for i in liste_insts:
	nom_classe = i.__name__#nom_classe = str(i).split("'")[1].split('.')[1]
	s = f"""
class MODULE_{nom_classe}(Module_Mdl):	#	A+B
	nom = "inst:{i.nom}"
	X, Y = {list(i.X)}, [0]
	X_noms, Y_noms = {["X" for _ in i.X]}, ["Y"]
	params = {{
	"""
	for p in i.params_str:
		s += f"""
		'{p}' : 0,"""
	s += f"""
	}}
	def cree_ix(self):
		#	Params
		X = self.X
		Y = self.Y[0]
		params = [p for _,p in self.params.items()]

		#	------------------

		self.ix = [
			{{'i':{nom_classe}, 'X':X,'x':{[None for _ in i.X]}, 'xt':{[None for _ in i.X]}, 'y':Y, 'p':params, 'sortie':True, '0':0}}
		]

		for i in range(len(self.ix)):
			assert self.ix[i][str(i)] == i

	def module_vers_model(self):
		self.cree_ix()
		self.insts_et_connections(ix)

modules_inst += [MODULE_{nom_classe}]
"""
	exec(s)