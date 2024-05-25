#pragma once

#include "insts.cuh"

#define pool2_1d__Xs 1
#define pool2_1d__PARAMS 0
#define pool2_1d_nom "simple Y"

uint Y__calculer_P(uint X[MAX_XS], uint x[MAX_XS], uint t[MAX_XS], uint Y, uint params[MAX_PARAMS]);
uint Y__calculer_L(uint X[MAX_XS], uint x[MAX_XS], uint t[MAX_XS], uint Y, uint params[MAX_PARAMS]);

void Y__init_poids(Inst_t * inst);

void Y__f(Inst_t * inst, float ** x__d, uint * ts__d, uint mega_t);
void Y__df(Inst_t * inst, float ** x__d, float ** dx__d, uint * ts__d, uint mega_t);