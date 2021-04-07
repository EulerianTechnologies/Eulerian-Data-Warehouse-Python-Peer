GET {
  TIMERANGE { 1594591200 1594592200 } 
  READERS   { ea:clickview@demo-fr AS clickview } 
  OUTPUTS_DISTINCT( clickview ) {
    clickview.uid, 
    clickview.type, 
    clickview.channel.odmedia, 
    clickview.timestamp
  }
};
