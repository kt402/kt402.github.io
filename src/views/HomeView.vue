<template>
  <div class="home">
<!--    <Accordion :multiple="true" :activeIndex="0">-->
<!--      <AccordionTab header="Lords Elites">-->
<!--        <RecView group="lords_elites"/>-->
<!--      </AccordionTab>-->
<!--      <AccordionTab header="Members">-->
<!--        <RecView group="members"/>-->
<!--      </AccordionTab>-->
<!--    </Accordion>-->
    <RecView group="rec_group_1" />
  </div>
</template>

<script lang="ts">

import { Options, Vue } from 'vue-class-component';
import RecView from "@/views/RecView.vue";
import TabView from "primevue/tabview";
import TabPanel from "primevue/tabpanel";
import Button from 'primevue/button';
import Accordion from 'primevue/accordion';
import AccordionTab from 'primevue/accordiontab';

@Options({
  components: {
    RecView, TabView, TabPanel, Button, AccordionTab, Accordion
  },
})
export default class HomeView extends Vue {
  tabs = [
    {
      title: 'Lords and Elites',
      key: 'rec_group_1',
    },
    {
      title: 'Members',
      key: 'rec_group_2',
    },

  ]
}

</script>

<style lang="scss">

</style>
