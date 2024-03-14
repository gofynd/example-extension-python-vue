<template>
    <div> 
      <h3>Partners Extension Admin Page</h3>
      <div>
        <div>Theme List Data</div>
        <pre id="data"></pre>
      </div>
    </div>    
</template>

<script>
import MainService from "./../services/main-service";

export default {
  name: 'admin_page',
  mounted: async () => {
    document.getElementById("data").innerHTML = JSON.stringify(await MainService.getThemeList(), null, 2);
  }
}
</script>

<style lang="less">

</style>
