import casadi as ca
import do_mpc
from matplotlib import pyplot as plt


def template_model():
    """
    Here could be the doc
    """
    model_type = "continuous"  # either 'discrete' or 'continuous'
    symvar_type = "SX"
    model = do_mpc.model.Model(model_type, symvar_type
    # ... "
    
    
    # Constants
    e0_greek_rho_Ldummy = 45.95
    e0_M_i1 = 0.046069
    # ... "
    
    # Dynamic/Differential states
    e0_HU_st0_i1 = model.set_variable(var_type='_x', var_name="e0_HU_st0_i1", shape=(1,1))  # noqa: E501
    e0_HU_st0_i2 = model.set_variable(var_type='_x', var_name="e0_HU_st0_i2", shape=(1,1))  # noqa: E501
    # ... "
    
    # Algebraic states
    e0_P_LV_st0_i1 = model.set_variable(var_type='_z', var_name="e0_P_LV_st0_i1", shape=(1,1))  # noqa: E501
    e0_P_LV_st0_i2 = model.set_variable(var_type='_z', var_name="e0_P_LV_st0_i2", shape=(1,1))  # noqa: E501
    # ... "
    
    
    # Control inputs 
    e0_greek_sigma_R = model.set_variable(var_type='_u', var_name="e0_greek_sigma_R")  # noqa: E501
    e0_greek_eta_L_st1 = model.set_variable(var_type='_u', var_name="e0_greek_eta_L_st1")  # noqa: E501
    # ... "
    
    # Parameters
    EQ_diff1 = ((((e0_F_V_st1*e0_y_st1_i1)-(e0_F_V_st0*e0_y_st0_i1))-(e0_F_L_st0*e0_x_st0_i1))-(e0_F_P_st0*e0_x_st0_i1))  # noqa: E501,E226
    EQ_diff2 = ((((e0_F_V_st1*e0_y_st1_i2)-(e0_F_V_st0*e0_y_st0_i2))-(e0_F_L_st0*e0_x_st0_i2))-(e0_F_P_st0*e0_x_st0_i2))  # noqa: E501,E226
    # ... "
    
    order_state_var = ["e0_HU_st0_i1", "e0_HU_st0_i2", "e0_HU_st0_i3", "e0_HU_st1_i1", "e0_HU_st2_i1", "e0_HU_st3_i1", "e0_HU_st4_i1", "e0_HU_st5_i1", "e0_HU_st6_i1", "e0_HU_st7_i1", "e0_HU_st8_i1", "e0_HU_st1_i2", "e0_HU_st2_i2", "e0_HU_st3_i2", "e0_HU_st4_i2", "e0_HU_st5_i2", "e0_HU_st6_i2", "e0_HU_st7_i2", "e0_HU_st8_i2", "e0_HU_st1_i3", "e0_HU_st2_i3", "e0_HU_st3_i3", "e0_HU_st4_i3", "e0_HU_st5_i3", "e0_HU_st6_i3", "e0_HU_st7_i3", "e0_HU_st8_i3", "e0_U_st1", "e0_U_st2", "e0_U_st3", "e0_U_st4", "e0_U_st5", "e0_U_st6", "e0_U_st7", "e0_U_st0", "e0_U_st8", "e0_HU_st9_i1", "e0_HU_st9_i2", "e0_HU_st9_i3", "e0_U_st9", ]  # noqa: E501
    order_eqs_diff = {"e0_HU_st0_i1": EQ_diff1, "e0_HU_st0_i2": EQ_diff2, "e0_HU_st0_i3": EQ_diff3, "e0_U_st0": EQ_diff4, "e0_HU_st1_i1": EQ_diff5, "e0_HU_st2_i1": EQ_diff6, "e0_HU_st3_i1": EQ_diff7, "e0_HU_st4_i1": EQ_diff8, "e0_HU_st5_i1": EQ_diff9, "e0_HU_st6_i1": EQ_diff10, "e0_HU_st7_i1": EQ_diff11, "e0_HU_st8_i1": EQ_diff12, "e0_HU_st1_i2": EQ_diff13, "e0_HU_st2_i2": EQ_diff14, "e0_HU_st3_i2": EQ_diff15, "e0_HU_st4_i2": EQ_diff16, "e0_HU_st5_i2": EQ_diff17, "e0_HU_st6_i2": EQ_diff18, "e0_HU_st7_i2": EQ_diff19, "e0_HU_st8_i2": EQ_diff20, "e0_HU_st1_i3": EQ_diff21, "e0_HU_st2_i3": EQ_diff22, "e0_HU_st3_i3": EQ_diff23, "e0_HU_st4_i3": EQ_diff24, "e0_HU_st5_i3": EQ_diff25, "e0_HU_st6_i3": EQ_diff26, "e0_HU_st7_i3": EQ_diff27, "e0_HU_st8_i3": EQ_diff28, "e0_U_st1": EQ_diff29, "e0_U_st2": EQ_diff30, "e0_U_st3": EQ_diff31, "e0_U_st4": EQ_diff32, "e0_U_st5": EQ_diff33, "e0_U_st6": EQ_diff34, "e0_U_st7": EQ_diff35, "e0_U_st8": EQ_diff36, "e0_HU_st9_i1": EQ_diff37, "e0_HU_st9_i2": EQ_diff38, "e0_HU_st9_i3": EQ_diff39, "e0_U_st9": EQ_diff40, }  # noqa: E501

    for state_var_name in order_state_var:
        model.set_rhs(state_var_name, order_eqs_diff[state_var_name])

    dict_algebraic_equations = {"EQ_alg41": EQ_alg41,"EQ_alg42": EQ_alg42,"EQ_alg43": EQ_alg43,"EQ_alg44": EQ_alg44,"EQ_alg45": EQ_alg45,"EQ_alg46": EQ_alg46,"EQ_alg47": EQ_alg47,"EQ_alg48": EQ_alg48,"EQ_alg49": EQ_alg49,"EQ_alg50": EQ_alg50,"EQ_alg51": EQ_alg51,"EQ_alg52": EQ_alg52,"EQ_alg53": EQ_alg53,"EQ_alg54": EQ_alg54,"EQ_alg55": EQ_alg55,"EQ_alg56": EQ_alg56,"EQ_alg57": EQ_alg57,"EQ_alg58": EQ_alg58,"EQ_alg59": EQ_alg59,"EQ_alg60": EQ_alg60,"EQ_alg61": EQ_alg61,"EQ_alg62": EQ_alg62,"EQ_alg63": EQ_alg63,"EQ_alg64": EQ_alg64,"EQ_alg65": EQ_alg65,"EQ_alg66": EQ_alg66,"EQ_alg67": EQ_alg67,"EQ_alg68": EQ_alg68,"EQ_alg69": EQ_alg69,"EQ_alg70": EQ_alg70,"EQ_alg71": EQ_alg71,"EQ_alg72": EQ_alg72,"EQ_alg73": EQ_alg73,"EQ_alg74": EQ_alg74,"EQ_alg75": EQ_alg75,"EQ_alg76": EQ_alg76,"EQ_alg77": EQ_alg77,"EQ_alg78": EQ_alg78,"EQ_alg79": EQ_alg79,"EQ_alg80": EQ_alg80,"EQ_alg81": EQ_alg81,"EQ_alg82": EQ_alg82,"EQ_alg83": EQ_alg83,"EQ_alg84": EQ_alg84,"EQ_alg85": EQ_alg85,"EQ_alg86": EQ_alg86,"EQ_alg87": EQ_alg87,"EQ_alg88": EQ_alg88,"EQ_alg89": EQ_alg89,"EQ_alg90": EQ_alg90,"EQ_alg91": EQ_alg91,"EQ_alg92": EQ_alg92,"EQ_alg93": EQ_alg93,"EQ_alg94": EQ_alg94,"EQ_alg95": EQ_alg95,"EQ_alg96": EQ_alg96,"EQ_alg97": EQ_alg97,"EQ_alg98": EQ_alg98,"EQ_alg99": EQ_alg99,"EQ_alg100": EQ_alg100,"EQ_alg101": EQ_alg101,"EQ_alg102": EQ_alg102,"EQ_alg103": EQ_alg103,"EQ_alg104": EQ_alg104,"EQ_alg105": EQ_alg105,"EQ_alg106": EQ_alg106,"EQ_alg107": EQ_alg107,"EQ_alg108": EQ_alg108,"EQ_alg109": EQ_alg109,"EQ_alg110": EQ_alg110,"EQ_alg111": EQ_alg111,"EQ_alg112": EQ_alg112,"EQ_alg113": EQ_alg113,"EQ_alg114": EQ_alg114,"EQ_alg115": EQ_alg115,"EQ_alg116": EQ_alg116,"EQ_alg117": EQ_alg117,"EQ_alg118": EQ_alg118,"EQ_alg119": EQ_alg119,"EQ_alg120": EQ_alg120,"EQ_alg121": EQ_alg121,"EQ_alg122": EQ_alg122,"EQ_alg123": EQ_alg123,"EQ_alg124": EQ_alg124,"EQ_alg125": EQ_alg125,"EQ_alg126": EQ_alg126,"EQ_alg127": EQ_alg127,"EQ_alg128": EQ_alg128,"EQ_alg129": EQ_alg129,"EQ_alg130": EQ_alg130,"EQ_alg131": EQ_alg131,"EQ_alg132": EQ_alg132,"EQ_alg133": EQ_alg133,"EQ_alg134": EQ_alg134,"EQ_alg135": EQ_alg135,"EQ_alg136": EQ_alg136,"EQ_alg137": EQ_alg137,"EQ_alg138": EQ_alg138,"EQ_alg139": EQ_alg139,"EQ_alg140": EQ_alg140,"EQ_alg141": EQ_alg141,"EQ_alg142": EQ_alg142,"EQ_alg143": EQ_alg143,"EQ_alg144": EQ_alg144,"EQ_alg145": EQ_alg145,"EQ_alg146": EQ_alg146,"EQ_alg147": EQ_alg147,"EQ_alg148": EQ_alg148,"EQ_alg149": EQ_alg149,"EQ_alg150": EQ_alg150,"EQ_alg151": EQ_alg151,"EQ_alg152": EQ_alg152,"EQ_alg153": EQ_alg153,"EQ_alg154": EQ_alg154,"EQ_alg155": EQ_alg155,"EQ_alg156": EQ_alg156,"EQ_alg157": EQ_alg157,"EQ_alg158": EQ_alg158,"EQ_alg159": EQ_alg159,"EQ_alg160": EQ_alg160,"EQ_alg161": EQ_alg161,"EQ_alg162": EQ_alg162,"EQ_alg163": EQ_alg163,"EQ_alg164": EQ_alg164,"EQ_alg165": EQ_alg165,"EQ_alg166": EQ_alg166,"EQ_alg167": EQ_alg167,"EQ_alg168": EQ_alg168,"EQ_alg169": EQ_alg169,"EQ_alg170": EQ_alg170,"EQ_alg171": EQ_alg171,"EQ_alg172": EQ_alg172,"EQ_alg173": EQ_alg173,"EQ_alg174": EQ_alg174,"EQ_alg175": EQ_alg175,"EQ_alg176": EQ_alg176,"EQ_alg177": EQ_alg177,"EQ_alg178": EQ_alg178,"EQ_alg179": EQ_alg179,"EQ_alg180": EQ_alg180,"EQ_alg181": EQ_alg181,"EQ_alg182": EQ_alg182,"EQ_alg183": EQ_alg183,"EQ_alg184": EQ_alg184,"EQ_alg185": EQ_alg185,"EQ_alg186": EQ_alg186,"EQ_alg187": EQ_alg187,"EQ_alg188": EQ_alg188,"EQ_alg189": EQ_alg189,"EQ_alg190": EQ_alg190,"EQ_alg191": EQ_alg191,"EQ_alg192": EQ_alg192,"EQ_alg193": EQ_alg193,"EQ_alg194": EQ_alg194,"EQ_alg195": EQ_alg195,"EQ_alg196": EQ_alg196,"EQ_alg197": EQ_alg197,"EQ_alg198": EQ_alg198,"EQ_alg199": EQ_alg199,"EQ_alg200": EQ_alg200,"EQ_alg201": EQ_alg201,"EQ_alg202": EQ_alg202,"EQ_alg203": EQ_alg203,"EQ_alg204": EQ_alg204,"EQ_alg205": EQ_alg205,"EQ_alg206": EQ_alg206,"EQ_alg207": EQ_alg207,"EQ_alg208": EQ_alg208,"EQ_alg209": EQ_alg209,"EQ_alg210": EQ_alg210,"EQ_alg211": EQ_alg211,"EQ_alg212": EQ_alg212,"EQ_alg213": EQ_alg213,"EQ_alg214": EQ_alg214,"EQ_alg215": EQ_alg215,"EQ_alg216": EQ_alg216,"EQ_alg217": EQ_alg217,"EQ_alg218": EQ_alg218,"EQ_alg219": EQ_alg219,"EQ_alg220": EQ_alg220,"EQ_alg221": EQ_alg221,"EQ_alg222": EQ_alg222,"EQ_alg223": EQ_alg223,"EQ_alg224": EQ_alg224,"EQ_alg225": EQ_alg225,"EQ_alg226": EQ_alg226,"EQ_alg227": EQ_alg227,"EQ_alg228": EQ_alg228,"EQ_alg229": EQ_alg229,"EQ_alg230": EQ_alg230,"EQ_alg231": EQ_alg231,"EQ_alg232": EQ_alg232,"EQ_alg233": EQ_alg233,"EQ_alg234": EQ_alg234,"EQ_alg235": EQ_alg235,"EQ_alg236": EQ_alg236,"EQ_alg237": EQ_alg237,"EQ_alg238": EQ_alg238,"EQ_alg239": EQ_alg239,"EQ_alg240": EQ_alg240,"EQ_alg241": EQ_alg241,"EQ_alg242": EQ_alg242,"EQ_alg243": EQ_alg243,"EQ_alg244": EQ_alg244,"EQ_alg245": EQ_alg245,"EQ_alg246": EQ_alg246,"EQ_alg247": EQ_alg247,"EQ_alg248": EQ_alg248,"EQ_alg249": EQ_alg249,"EQ_alg250": EQ_alg250,"EQ_alg251": EQ_alg251,"EQ_alg252": EQ_alg252,"EQ_alg253": EQ_alg253,"EQ_alg254": EQ_alg254,"EQ_alg255": EQ_alg255,"EQ_alg256": EQ_alg256,"EQ_alg257": EQ_alg257,"EQ_alg258": EQ_alg258,"EQ_alg259": EQ_alg259,"EQ_alg260": EQ_alg260,"EQ_alg261": EQ_alg261,"EQ_alg262": EQ_alg262,"EQ_alg263": EQ_alg263,"EQ_alg264": EQ_alg264,"EQ_alg265": EQ_alg265,"EQ_alg266": EQ_alg266,"EQ_alg267": EQ_alg267,"EQ_alg268": EQ_alg268,"EQ_alg269": EQ_alg269,"EQ_alg270": EQ_alg270,"EQ_alg271": EQ_alg271,"EQ_alg272": EQ_alg272,"EQ_alg273": EQ_alg273,"EQ_alg274": EQ_alg274,"EQ_alg275": EQ_alg275,"EQ_alg276": EQ_alg276,"EQ_alg277": EQ_alg277,"EQ_alg278": EQ_alg278,"EQ_alg279": EQ_alg279,"EQ_alg280": EQ_alg280,"EQ_alg281": EQ_alg281,"EQ_alg282": EQ_alg282,"EQ_alg283": EQ_alg283,"EQ_alg284": EQ_alg284,"EQ_alg285": EQ_alg285,"EQ_alg286": EQ_alg286,"EQ_alg287": EQ_alg287,"EQ_alg288": EQ_alg288,"EQ_alg289": EQ_alg289,"EQ_alg290": EQ_alg290,"EQ_alg291": EQ_alg291,"EQ_alg292": EQ_alg292,"EQ_alg293": EQ_alg293,"EQ_alg294": EQ_alg294,"EQ_alg295": EQ_alg295,"EQ_alg296": EQ_alg296,"EQ_alg297": EQ_alg297,"EQ_alg298": EQ_alg298,"EQ_alg299": EQ_alg299,"EQ_alg300": EQ_alg300,"EQ_alg301": EQ_alg301,"EQ_alg302": EQ_alg302,"EQ_alg303": EQ_alg303,"EQ_alg304": EQ_alg304,"EQ_alg305": EQ_alg305,"EQ_alg306": EQ_alg306,"EQ_alg307": EQ_alg307,"EQ_alg308": EQ_alg308,"EQ_alg309": EQ_alg309,"EQ_alg310": EQ_alg310,"EQ_alg311": EQ_alg311,"EQ_alg312": EQ_alg312,"EQ_alg313": EQ_alg313,"EQ_alg314": EQ_alg314,"EQ_alg315": EQ_alg315,"EQ_alg316": EQ_alg316,"EQ_alg317": EQ_alg317,"EQ_alg318": EQ_alg318,"EQ_alg319": EQ_alg319,"EQ_alg320": EQ_alg320,"EQ_alg321": EQ_alg321,"EQ_alg322": EQ_alg322,"EQ_alg323": EQ_alg323,"EQ_alg324": EQ_alg324,"EQ_alg325": EQ_alg325,"EQ_alg326": EQ_alg326,"EQ_alg327": EQ_alg327,"EQ_alg328": EQ_alg328,"EQ_alg329": EQ_alg329,"EQ_alg330": EQ_alg330,"EQ_alg331": EQ_alg331,"EQ_alg332": EQ_alg332,"EQ_alg333": EQ_alg333,"EQ_alg334": EQ_alg334,"EQ_alg335": EQ_alg335,"EQ_alg336": EQ_alg336,"EQ_alg337": EQ_alg337,"EQ_alg338": EQ_alg338,"EQ_alg339": EQ_alg339,"EQ_alg340": EQ_alg340,"EQ_alg341": EQ_alg341,"EQ_alg342": EQ_alg342,"EQ_alg343": EQ_alg343,"EQ_alg344": EQ_alg344,"EQ_alg345": EQ_alg345,"EQ_alg346": EQ_alg346,"EQ_alg347": EQ_alg347,"EQ_alg348": EQ_alg348,"EQ_alg349": EQ_alg349,"EQ_alg350": EQ_alg350,"EQ_alg351": EQ_alg351,"EQ_alg352": EQ_alg352,"EQ_alg353": EQ_alg353,"EQ_alg354": EQ_alg354,"EQ_alg355": EQ_alg355,"EQ_alg356": EQ_alg356,"EQ_alg357": EQ_alg357,"EQ_alg358": EQ_alg358,"EQ_alg359": EQ_alg359,"EQ_alg360": EQ_alg360,"EQ_alg361": EQ_alg361,"EQ_alg362": EQ_alg362,"EQ_alg363": EQ_alg363,"EQ_alg364": EQ_alg364,"EQ_alg365": EQ_alg365,"EQ_alg366": EQ_alg366,"EQ_alg367": EQ_alg367,"EQ_alg368": EQ_alg368,"EQ_alg369": EQ_alg369,"EQ_alg370": EQ_alg370,"EQ_alg371": EQ_alg371,"EQ_alg372": EQ_alg372,"EQ_alg373": EQ_alg373,"EQ_alg374": EQ_alg374,"EQ_alg375": EQ_alg375,"EQ_alg376": EQ_alg376,"EQ_alg377": EQ_alg377,"EQ_alg378": EQ_alg378,"EQ_alg379": EQ_alg379,"EQ_alg380": EQ_alg380,"EQ_alg381": EQ_alg381,"EQ_alg382": EQ_alg382,"EQ_alg383": EQ_alg383,"EQ_alg384": EQ_alg384,"EQ_alg385": EQ_alg385,"EQ_alg386": EQ_alg386,"EQ_alg387": EQ_alg387,"EQ_alg388": EQ_alg388,"EQ_alg389": EQ_alg389,"EQ_alg390": EQ_alg390,"EQ_alg391": EQ_alg391,"EQ_alg392": EQ_alg392,"EQ_alg393": EQ_alg393,"EQ_alg394": EQ_alg394,"EQ_alg395": EQ_alg395,"EQ_alg396": EQ_alg396,"EQ_alg397": EQ_alg397,"EQ_alg398": EQ_alg398,"EQ_alg399": EQ_alg399,"EQ_alg400": EQ_alg400,"EQ_alg401": EQ_alg401,"EQ_alg402": EQ_alg402,"EQ_alg403": EQ_alg403,"EQ_alg404": EQ_alg404,"EQ_alg405": EQ_alg405,"EQ_alg406": EQ_alg406,"EQ_alg407": EQ_alg407,"EQ_alg408": EQ_alg408,"EQ_alg409": EQ_alg409,"EQ_alg410": EQ_alg410,"EQ_alg411": EQ_alg411,"EQ_alg412": EQ_alg412,"EQ_alg413": EQ_alg413,"EQ_alg414": EQ_alg414,"EQ_alg415": EQ_alg415,"EQ_alg416": EQ_alg416,"EQ_alg417": EQ_alg417,"EQ_alg418": EQ_alg418,}  # noqa: E501
    try:
        Eq_fun_e0_h_LVN2_st9_i2 = e0_h_LVN2_st9_i2 - fun_179299__polynomial4(e0_T_N2_st9,e0_Param_hLV_A_i2,e0_Param_hLV_B_i2,e0_Param_hLV_C_i2,e0_Param_hLV_D_i2,e0_Param_hLV_E_i2)  # noqa: E501,E231
        dict_algebraic_equations["Eq_fun_e0_h_LVN2_st9_i2"] = Eq_fun_e0_h_LVN2_st9_i2  # noqa: E501
    except KeyError:
        pass
    # ... "    
    
    
    # fmt:on

    for alg_var_name, alg_eq in dict_algebraic_equations.items():
        model.set_alg(alg_var_name, alg_eq)

    # Build the model
    model.setup()

    return model

    simulator = do_mpc.simulator.Simulator(model)

    # tvp_num = simulator.get_tvp_template()
    # def tvp_fun(t_now):
    #     return tvp_num
    # simulator.set_tvp_fun(tvp_fun)

    # fmt:off


    
def template_simulator(model):
    """
    Here could be the doc
    """
    # Parameters
    p_template = simulator.get_p_template()

    simulator.set_p_fun(lambda t_now: p_template)
    # Initial conditions (x0)
    simulator.x0["e0_HU_st0_i1"] = -4.3628597E-6
    # ... "
    
    
    # Initial condition (z0)
    simulator.z0["e0_P_LV_st0_i1"] = 0.08850626933441658
    simulator.z0["e0_P_LV_st0_i2"] = 0.03539382722579711
    simulator.z0["e0_P_LV_st1_i1"] = 0.08850626933441658
    # ... "
    
    simulator.u0["e0_greek_sigma_R"] = 1.0
    simulator.u0["e0_greek_eta_L_st1"] = 0.0019
    simulator.u0["e0_greek_eta_L_st2"] = 0.0019
    # ... "
    
    # fmt:on
    return simulator
    
    
    
    
    
    
    
    
    
