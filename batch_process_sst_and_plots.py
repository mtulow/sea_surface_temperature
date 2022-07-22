# batch_process_sst_and_plots.py
################################################################
# All regions are processed in a loop
#################################################################
# define regions to process
region_list =["New_Zealand_Northland", "New_Zealand_Taranaki", "New_Zealand_East_Cape",
              "Australia_QLD_Brisbane", "Australia_QLD_central", "Australia_QLD_northern",
              "Australia_NSW_Sydney", "Australia_Tasmania", "Costa_Rica", "Baja_Sur",
              "California", "Gulf_of_Maine", "US_Central_Bight", "Florida"]


# to process one or more only ...
import plot_SST_map
region_list = ["New_Zealand", "California"]
for region in region_list:
    sst_ds = plot_SST_map.get_dataset(region)
    plot_SST_map.plot_map(sst_ds)
    
