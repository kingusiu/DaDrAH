{'_self_setattr_tracking': True, '_trainable': True, '_stateful': False, 'built': True, '_build_input_shape': TensorShape([None, 1]), 
'_saved_model_inputs_spec': TensorSpec(shape=(None, 1), dtype=tf.float32, name='input_1'), '_input_spec': None, 
'_supports_masking': True, '_name': 'custom__train__step__model', '_activity_regularizer': None, '_trainable_weights': [], 
'_non_trainable_weights': [], '_updates': [], '_thread_local': <_thread._local object at 0x7f929052bd00>, '_callable_losses': [], 
'_losses': [], '_metrics': [], '_metrics_lock': <unlocked _thread.lock object at 0x7f9273fea440>, '_dtype_policy': <Policy "float32", loss_scale=None>, 
'_dtype_defaulted_to_floatx': True, '_compute_dtype_object': tf.float32, '_autocast': False, 
'_layers': [<tensorflow.python.keras.engine.input_layer.InputLayer object at 0x7f9278015eb8>, 
            <tensorflow.python.keras.layers.core.Dense object at 0x7f928f68b748>, 
            <tensorflow.python.keras.layers.core.Dense object at 0x7f9273fd4c18>, 
            <tensorflow.python.keras.layers.core.Dense object at 0x7f9273f930b8>, 
            <tensorflow.python.keras.layers.core.Dense object at 0x7f9273f93dd8>, 
            <tensorflow.python.keras.layers.core.Dense object at 0x7f9273fae8d0>, 
            <tensorflow.python.keras.layers.core.Dense object at 0x7f9273fb6438>], 
'_inbound_nodes': [], '_outbound_nodes': [], '_expects_training_arg': True, '_default_training_arg': None, 
'_expects_mask_arg': True, '_dynamic': False, '_initial_weights': None, '_auto_track_sub_layers': True, 
'_is_graph_network': True, 'inputs': [<tf.Tensor 'input_1:0' shape=(None, 1) dtype=float32>], 'outputs': [<tf.Tensor 'dense_5/BiasAdd:0' shape=(None, 1) dtype=float32>], 
'input_names': ['input_1'], 'output_names': ['dense_5'], '_compute_output_and_mask_jointly': True, '_distribution_strategy': None, 
'test_function': None, 'predict_function': None, '_compiled_trainable_state': <WeakKeyDictionary at 0x7f926d3b77f0>, '_training_state': None, 
'_trackable_saver': <tensorflow.python.training.tracking.util.TrackableSaver object at 0x7f9273fbba58>, 
'_steps_per_execution': <tf.Variable 'Variable:0' shape=() dtype=int64, numpy=1>, 
'_train_counter': <tf.Variable 'Variable:0' shape=() dtype=int64, numpy=39>, 
'_test_counter': <tf.Variable 'Variable:0' shape=() dtype=int64, numpy=0>, 
'_predict_counter': <tf.Variable 'Variable:0' shape=() dtype=int64, numpy=0>, 
'_base_model_initialized': True, '_nested_inputs': <tf.Tensor 'input_1:0' shape=(None, 1) dtype=float32>, 
'_nested_outputs': <tf.Tensor 'dense_5/BiasAdd:0' shape=(None, 1) dtype=float32>, '_enable_dict_to_input_mapping': True, 
'_input_layers': [<tensorflow.python.keras.engine.input_layer.InputLayer object at 0x7f9278015eb8>], '_output_layers': [<tensorflow.python.keras.layers.core.Dense object at 0x7f9273fb6438>], 
'_input_coordinates': [(<tensorflow.python.keras.engine.input_layer.InputLayer object at 0x7f9278015eb8>, 0, 0)], 
'_output_coordinates': [(<tensorflow.python.keras.layers.core.Dense object at 0x7f9273fb6438>, 0, 0)], 
'_output_mask_cache': {}, '_output_tensor_cache': {}, '_output_shape_cache': {}, '_network_nodes': {'dense_4_ib-0', 'dense_5_ib-0', 'dense_3_ib-0', 'input_1_ib-0', 'dense_ib-0', 'dense_1_ib-0', 'dense_2_ib-0'}, 
'_nodes_by_depth': defaultdict(<class 'list'>, {0: [<tensorflow.python.keras.engine.node.Node object at 0x7f9273fbba90>], 
                                                1: [<tensorflow.python.keras.engine.node.Node object at 0x7f9273fb6fd0>], 
                                                2: [<tensorflow.python.keras.engine.node.Node object at 0x7f9273fb6710>], 
                                                3: [<tensorflow.python.keras.engine.node.Node object at 0x7f9273faeba8>], 
                                                4: [<tensorflow.python.keras.engine.node.Node object at 0x7f9273f93da0>], 
                                                5: [<tensorflow.python.keras.engine.node.Node object at 0x7f9273f93438>], 
                                                6: [<tensorflow.python.keras.engine.node.Node object at 0x7f92872ec240>]}), 
'_layer_call_argspecs': {<tensorflow.python.keras.engine.input_layer.InputLayer object at 0x7f9278015eb8>: FullArgSpec(args=['self', 'inputs'], varargs=None, varkw='kwargs', defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={}), 
                        <tensorflow.python.keras.layers.core.Dense object at 0x7f928f68b748>: FullArgSpec(args=['self', 'inputs'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={}), 
                        <tensorflow.python.keras.layers.core.Dense object at 0x7f9273fd4c18>: FullArgSpec(args=['self', 'inputs'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={}), 
                        <tensorflow.python.keras.layers.core.Dense object at 0x7f9273f930b8>: FullArgSpec(args=['self', 'inputs'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={}), 
                        <tensorflow.python.keras.layers.core.Dense object at 0x7f9273f93dd8>: FullArgSpec(args=['self', 'inputs'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={}), 
                        <tensorflow.python.keras.layers.core.Dense object at 0x7f9273fae8d0>: FullArgSpec(args=['self', 'inputs'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={}), 
                        <tensorflow.python.keras.layers.core.Dense object at 0x7f9273fb6438>: FullArgSpec(args=['self', 'inputs'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={})}, 
'_feed_input_names': ['input_1'], '_feed_inputs': [<tf.Tensor 'input_1:0' shape=(None, 1) dtype=float32>], '_feed_input_shapes': [(None, 1)], 
'_tensor_usage_count': Counter({'140266987933424': 1, '140266987666568': 1, '140266987775872': 1, '140266987807464': 1, '140266987810320': 1, '140266987829624': 1, '140266874565800': 1}), 
'_obj_reference_counts_dict': ObjectIdentityDictionary({<_ObjectIdentityWrapper wrapping True>: 2, 
                                                        <_ObjectIdentityWrapper wrapping <tensorflow.python.keras.optimizer_v2.adam.Adam object at 0x7f9278015198>>: 1, 
                                                        <_ObjectIdentityWrapper wrapping <tensorflow.python.keras.engine.compile_utils.LossesContainer object at 0x7f928b5f40f0>>: 1, 
                                                        <_ObjectIdentityWrapper wrapping <tensorflow.python.keras.engine.compile_utils.MetricsContainer object at 0x7f926d3b7780>>: 1, 
                                                        <_ObjectIdentityWrapper wrapping <function quantile_loss.<locals>.loss at 0x7f9278031048>>: 1, 
                                                        <_ObjectIdentityWrapper wrapping <tensorflow.python.keras.callbacks.History object at 0x7f926d30b5f8>>: 1, 
                                                        <_ObjectIdentityWrapper wrapping <function Model.make_train_function.<locals>.train_function at 0x7f926d36d510>>: 1}), 
'_run_eagerly': True, '_self_unconditional_checkpoint_dependencies': [TrackableReference(name='optimizer', ref=<tensorflow.python.keras.optimizer_v2.adam.Adam object at 0x7f9278015198>)], 
'_self_unconditional_dependency_names': {'optimizer': <tensorflow.python.keras.optimizer_v2.adam.Adam object at 0x7f9278015198>}, 
'_self_unconditional_deferred_dependencies': {}, '_self_update_uid': -1, '_self_name_based_restores': set(), '_self_saveable_object_factories': {}, 
'optimizer': <tensorflow.python.keras.optimizer_v2.adam.Adam object at 0x7f9278015198>, 
'compiled_loss': <tensorflow.python.keras.engine.compile_utils.LossesContainer object at 0x7f928b5f40f0>, 
'compiled_metrics': <tensorflow.python.keras.engine.compile_utils.MetricsContainer object at 0x7f926d3b7780>, 
'_is_compiled': True, 'loss': <function quantile_loss.<locals>.loss at 0x7f9278031048>, 
'history': <tensorflow.python.keras.callbacks.History object at 0x7f926d30b5f8>, 'stop_training': False, 'train_function': <function Model.make_train_function.<locals>.train_function at 0x7f926d36d510>}