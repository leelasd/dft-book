from jasp import *
from ase.io import write
with jasp('surfaces/Pt-slab') as calc:
    atoms = calc.get_atoms()
    e_slab = atoms.get_potential_energy()
write('images/pt-slab.png', atoms,show_unit_cell=2)
with jasp('surfaces/Pt-slab-O-fcc') as calc:
    atoms = calc.get_atoms()
    e_slab_o_fcc = atoms.get_potential_energy()
write('images/pt-slab-fcc-o.png', atoms,show_unit_cell=2)
with jasp('surfaces/Pt-slab-O-hcp') as calc:
    atoms = calc.get_atoms()
    e_slab_o_hcp = atoms.get_potential_energy()
write('images/pt-slab-hcp-o.png', atoms,show_unit_cell=2)
with jasp('surfaces/Pt-slab-O-bridge') as calc:
    atoms = calc.get_atoms()
    e_slab_o_bridge = atoms.get_potential_energy()
write('images/pt-slab-bridge-o.png', atoms,show_unit_cell=2)
with jasp('molecules/O2-sp-triplet-350') as calc:
    atoms = calc.get_atoms()
    e_O2 = atoms.get_potential_energy()
Hads_fcc = e_slab_o_fcc - e_slab - 0.5 * e_O2
Hads_hcp = e_slab_o_hcp - e_slab - 0.5 * e_O2
Hads_bridge = e_slab_o_bridge - e_slab - 0.5 * e_O2
print 'Hads (fcc)    = {0} eV/O'.format(Hads_fcc)
print 'Hads (hcp)    = {0} eV/O'.format(Hads_hcp)
print 'Hads (bridge) = {0} eV/O'.format(Hads_bridge)