from __future__ import annotations

from typing import TYPE_CHECKING

import ba,_ba
from bastd.gameutils import SharedObjects

if TYPE_CHECKING:
    from typing import Any, List, Dict

# This file was automatically generated from "big_g.ma"
# pylint: disable=all
class mapdefs:
    points = {}
    # noinspection PyDictCreation
    boxes = {}
    boxes['area_of_interest_bounds'] = (-1.4011866709, -1.331310176,
                                        -4.5426286416) + (0.0, 0.0, 0.0) + (
                                            19.11746262, 10.19675564, 25.50119277)
    points['ffa_spawn1'] = (3.140826121, -1.16512015,
                            6.172121491) + (4.739204545, 1-1.0, 1.028864849)
    points['ffa_spawn2'] = (5.416289073, -1.180022599, -0.1696495695) + (
        2.945888237, -0.621599724, 0.4969830881)
    points['ffa_spawn3'] = (-0.3692088357, -1.88984723, -6.909741615) + (
        7.575371952, 0.621599724, 0.4969830881)
    points['ffa_spawn4'] = (-2.391932409, -1.123690253, -3.417262271) + (
        2.933065031, 0.621599724, 0.9796558695)
    points['ffa_spawn5'] = (-7.46052038, -1.863807079,
                            4.936420902) + (0.8707600789, -0.621599724, 2.233577195)
    points['flag1'] = (7.557928387, 2.889342613, -7.208799596)
    points['flag2'] = (7.696183956, 1.095466627, 6.103380446)
    points['flag3'] = (-8.122819332, 2.844893069, 6.103380446)
    points['flag4'] = (-8.018537918, 2.844893069, -6.202403896)
    points['flag_default'] = (-7.563673017, 2.850652319, 0.08844978098)
    boxes['map_bounds'] = (-7.1916036665, -3.764115729, -43.1971423239) + (
        0.0, 0.0, 0.0) + (48.41996888, 100.47258973, 150.17335735)
    points['powerup_spawn1'] = (7.830495287, -1.115087683, -0.05452287857)
    points['powerup_spawn2'] = (-5.190293739, -1.476317443, -3.80237889)
    points['powerup_spawn3'] = (-8.540957726, -1.762979519, -7.27710542)
    points['powerup_spawn4'] = (7.374052727, -1.762979519, -3.091707631)
    points['powerup_spawn5'] = (-8.691423338, -1.692026034, 6.627877455)
    points['race_mine1'] = (-0.06161453294, 1.123140909, 4.966104324)
    points['race_mine10'] = (-6.870248758, 2.851484105, 2.718992803)
    points['race_mine2'] = (-0.06161453294, 1.123140909, 6.99632996)
    points['race_mine3'] = (-0.7319278377, 1.123140909, -2.828583367)
    points['race_mine4'] = (-3.286508423, 1.123140909, 0.8453899305)
    points['race_mine5'] = (5.077545429, 2.850225463, -5.253575631)
    points['race_mine6'] = (6.286453838, 2.850225463, -5.253575631)
    points['race_mine7'] = (0.969120762, 2.851484105, -7.892038145)
    points['race_mine8'] = (-2.976299166, 2.851484105, -6.241064664)
    points['race_mine9'] = (-6.962812986, 2.851484105, -2.120262964)
    points['race_point1'] = (2.280447713, 1.16512015, 6.015278429) + (
        0.7066894139, 4.672784871, 1.322422256)
    points['race_point10'] = (-4.196540687, 2.877461266, -7.106874334) + (
        0.1057202515, 5.496127671, 1.028552836)
    points['race_point11'] = (-7.634488499, 2.877461266, -3.61728743) + (
        1.438144134, 5.157457566, 0.06318119808)
    points['race_point12'] = (-7.541251512, 2.877461266, 3.290439202) + (
        1.668578284, 5.52484043, 0.06318119808)
    points['race_point2'] = (4.853459878, 1.16512015,
                            6.035867283) + (0.3920628436, 4.577066678, 1.34568243)
    points['race_point3'] = (6.905234402, 1.16512015, 1.143337503) + (
        1.611663691, 3.515259775, 0.1135135003)
    points['race_point4'] = (2.681673258, 1.16512015, 0.771967064) + (
        0.6475414982, 3.602143342, 0.1135135003)
    points['race_point5'] = (-0.3776550727, 1.225615225, 1.920343787) + (
        0.1057202515, 4.245024435, 0.5914887576)
    points['race_point6'] = (-4.365081958, 1.16512015, -0.3565529313) + (
        1.627090525, 4.549428479, 0.1135135003)
    points['race_point7'] = (0.4149308672, 1.16512015, -3.394316313) + (
        0.1057202515, 4.945367833, 1.310190117)
    points['race_point8'] = (4.27031635, 2.19747021, -3.335165617) + (
        0.1057202515, 4.389664492, 1.20413595)
    points['race_point9'] = (2.552998384, 2.877461266, -7.117366939) + (
        0.1057202515, 5.512312989, 0.9986814472)
    points['shadow_lower_bottom'] = (-0.2227795102, 0.2903873918, 2.680075641)
    points['shadow_lower_top'] = (-0.2227795102, 0.8824975157, 2.680075641)
    points['shadow_upper_bottom'] = (-0.2227795102, 6.305086402, 2.680075641)
    points['shadow_upper_top'] = (-0.2227795102, 9.470923628, 2.680075641)
    points['spawn1'] = (3.180043217, -3.85596295, -1.407134234) + (0.7629937742,
                                                                -1.0, 1.818908238)
    points['spawn2'] = (-5.880548999, -3.142163379, -2.171168951) + (1.817516622, -1.0,
                                                                0.7724344394)
    points['spawn_by_flag1'] = (7.180043217, 2.85596295,
                                -4.407134234) + (0.7629937742, 1.0, 1.818908238)
    points['spawn_by_flag2'] = (5.880548999, 1.142163379,
                                6.171168951) + (1.817516622, 1.0, 0.7724344394)
    points['spawn_by_flag3'] = (-6.66642559, 3.554416948,
                                5.820238985) + (1.097315815, 1.0, 1.285161684)
    points['spawn_by_flag4'] = (-6.842951255, 3.554416948,
                                -6.17429905) + (0.8208434737, 1.0, 1.285161684)
    points['tnt1'] = (-3.398312776, 2.067056737, -1.90142919)

class Desert(ba.Map):
    """Large G shaped map for racing"""

    defs = mapdefs

    name = 'Desert'

    @classmethod
    def get_play_types(cls) -> List[str]:
        """Return valid play types for this map."""
        return [
            'race', 'melee', 'keep_away', 'team_flag', 'king_of_the_hill',
            'conquest'
        ]

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'bigGPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: Dict[str, Any] = {
            'model_top': ba.getmodel('bigG'),
            'model_bottom': ba.getmodel('bigGBottom'),
            'model_bg': ba.getmodel('natureBackground'),
            'bg_vr_fill_model': ba.getmodel('natureBackgroundVRFill'),
            'collide_model': ba.getcollidemodel('bigGCollide'),
            'tex': ba.gettexture('bigG'),
            'model_bg_tex': ba.gettexture('natureBackgroundColor'),
            'collide_bg': ba.getcollidemodel('natureBackgroundCollide'),
            'bumper_collide_model': ba.getcollidemodel('bigGBumper'),
            'bg_material': ba.Material()
        }
        data['bg_material'].add_actions(actions=('modify_part_collision',
                                                 'friction', 3.0))
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()

        self.background = ba.newnode(
            'terrain',
            attrs={
                'model': self.preloaddata['model_bg'],
                'lighting': False,
                'background': True,
                'color_texture': self.preloaddata['model_bg_tex']
            })

        self.bg_collide = ba.newnode('terrain',
                                     attrs={
                                         'collide_model':
                                             self.preloaddata['collide_bg'],
                                         'materials': [
                                             shared.footing_material,
                                             self.preloaddata['bg_material'],
                                             
                                         ]
                                     })
        gnode = ba.getactivity().globalsnode
        gnode.tint = (1.1, 1.2, 1.3)
        gnode.ambient_color = (1.1, 1.2, 1.3)
        gnode.vignette_outer = (0.65, 0.6, 0.55)
        gnode.vignette_inner = (0.9, 0.9, 0.93)


ba._map.register_map(Desert)