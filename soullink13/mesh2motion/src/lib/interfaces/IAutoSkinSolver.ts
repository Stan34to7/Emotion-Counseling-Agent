import { BufferGeometry, Object3D } from 'three'
import { SkeletonType } from '../enums/SkeletonType.js'
import BoneTesterData from './BoneTesterData.js'

/**
 * 绑骨算法接口（旧版本兼容）
 */
export interface IAutoSkinSolver {
  set_geometry (geom: BufferGeometry): void
  set_show_debug (debug_value: boolean): void
  set_bone_index_to_test (bone_idx: number): void
  set_skeleton_type (skinning_type: SkeletonType): void
  set_debugging_scene_object (scene_object: Object3D): void
  calculate_indexes_and_weights (): number[][]
  test_bones_outside_in_mesh (): BoneTesterData
}
