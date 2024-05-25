#include "main.cuh"

#include "../impl_template/tmpl_etc.cu"

static void ___test_le_model(BTCUSDT_t * btcusdt, char * fichier) {
	printf(" ======================================================= \n");
	printf(" ============== %s ============== \n", fichier);
	printf(" ======================================================= \n");
	Mdl_t * mdl = cree_mdl_depuis_st_bin(fichier);
	tester_le_model(mdl, btcusdt);
	liberer_mdl(mdl);
};

void verif_mdl_1e5() {
	BTCUSDT_t * btcusdt = cree_btcusdt("prixs/dar_8x16.bin");
	//
	ASSERT(btcusdt->X == 128);
	ASSERT(btcusdt->Y ==   3);
	//
	//ASSERT(GRAND_T == 64);
	//ASSERT(MEGA_T  ==  8);
	//
	//___test_le_model(btcusdt, "mdl_test_inst/_00_activation.st.bin");			//OK
	//___test_le_model(btcusdt, "mdl_test_inst/_01_biais.st.bin");				//OK
	//___test_le_model(btcusdt, "mdl_test_inst/_02_kconvl2d_stricte.st.bin");	//OK
	//___test_le_model(btcusdt, "mdl_test_inst/_03_matmul1d.st.bin");			//OK
	//___test_le_model(btcusdt, "mdl_test_inst/_04_matmul1d_canal.st.bin");		//OK
	//___test_le_model(btcusdt, "mdl_test_inst/_05_mul2.st.bin");				//OK
	//___test_le_model(btcusdt, "mdl_test_inst/_06_mul3.st.bin");				//OK
	//___test_le_model(btcusdt, "mdl_test_inst/_07_pool2d.st.bin");
	//                                     08
	//___test_le_model(btcusdt, "mdl_test_inst/_09_somme2.st.bin");				//OK
	//___test_le_model(btcusdt, "mdl_test_inst/_10_somme3.st.bin");				//OK
	//___test_le_model(btcusdt, "mdl_test_inst/_11_somme4.st.bin");				//OK
	//
	liberer_btcusdt(btcusdt);
};