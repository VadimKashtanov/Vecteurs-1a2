#include "mdl.cuh"

#include "../../impl_template/tmpl_etc.cu"

void mdl_optimisation(Mdl_t * mdl) {
	mdl->BLOQUES = mdl->insts;
	mdl->elements = (uint*)malloc(sizeof(uint) * mdl->insts);
	FOR(0, i, mdl->insts)
		mdl->elements[i] = 0;
	mdl->instructions = (uint**)malloc(sizeof(uint*) * mdl->insts);
	FOR(0, i, mdl->insts)
		mdl->instructions[i] = (uint*)malloc(sizeof(uint) * mdl->insts);
	//
	uint a_été_inclue[mdl->insts];
	FOR(0, i, mdl->insts) a_été_inclue[i] = 0;
	
	//
	/*uint tous_inclues = 0;
	while (!(tous_inclues)) {
		FOR(0, i, mdl->insts) {
			if (!a_été_inclue[i]) {
				uint requière_une_donnee = false;
				FOR(0, _x, inst_Xs[mdl->inst[i]->ID]) {
					if (mdl->inst[i]->x_est_une_entree[_x]) requière_une_donnee = true;
				};
				if (requière_une_donnee) {
					mdl->elements[0]++;
					a_été_inclue[i] = 1;

					//	Ajout element
					mdl->instructions[0][mdl->elements[0]++] = i;
				}
			}
		}
		tous_inclues = 1;
		FOR(0, i, mdl->insts)
			if (!(a_été_inclue[i]))
				tous_inclues = 0;
	}*/
};