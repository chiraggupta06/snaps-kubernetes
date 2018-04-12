
import pluginbase
from provision.kubernetes.plugin.k8_impl import k8_utils
class Deploy(pluginbase.PluginBase):
    """Plugin Deploy class. It should be similar across all plugins
    """
    def execute (self,data, operation):
        ret = False;
        print "************ operation******** "
        print operation
        if (operation is "clean_k8"):
 	       ret=k8_utils.clean_k8(data, operation)
        elif (operation is "dynamic_deploy_k8"):
 	       ret=k8_utils.dynamic_node_add_and_del(data, operation)
        elif (operation is "dynamic_clean_k8"):
 	       ret=k8_utils.dynamic_node_add_and_del(data, operation)
 	       #ret=k8_utils.dynamic_deploy_nodes(data, operation)
 	       #ret=k8_utils.dynamic_clean_nodes(data, operation)
        elif (operation is "deploy_k8"):
 	      ret=k8_utils.main(data, operation)

        return ret