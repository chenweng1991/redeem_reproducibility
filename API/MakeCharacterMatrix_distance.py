"""
This module takes in allele table and generate cas tree pickle
The result can be read in like this for example
with open('tree.ILP.CD24_1.allele.pkl', 'rb') as f:
    tree=pickle.load(f)
---
Only one parameter which is the file name of the allele table
---
The output is pickle file that store the tree
"""
import pandas as pd
# import os
import sys
import cassiopeia as cas
import pickle

allele_file=sys.argv[1]
name=allele_file.replace('.allele','')
alleles=pd.read_csv("/lab/solexa_weissman/cweng/Projects/Collaborator/Dian/Yang_MKP2_230315/TS_redo/"+allele_file,sep=',')
cm, prior_probs,character_to_indels=cas.pp.convert_alleletable_to_character_matrix(alleles)
tree=cas.data.CassiopeiaTree(cm)
nj_solver = cas.solver.NeighborJoiningSolver(dissimilarity_function=cas.solver.dissimilarity.weighted_hamming_distance, add_root=True)
nj_solver.solve(tree, collapse_mutationless_edges=True)
Weighted_hm_distance=tree.get_dissimilarity_map()
cm.to_csv('CharacterMatrix.'+name)
Weighted_hm_distance.to_csv('weighted_hm_distance.'+name)
with open('tree.w.hm.'+name+'.pkl','wb') as f:
    pickle.dump(tree,f)  
