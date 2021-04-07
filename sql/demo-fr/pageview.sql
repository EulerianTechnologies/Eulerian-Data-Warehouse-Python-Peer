GET {
  TIMERANGE { 1594591200 1594592200 } 
  READERS   { ea:pageview@demo-fr AS pageview } 
  OUTPUTS_DISTINCT( pageview ) {
    pageview.uid,
    pageview.timestamp,
    pageview.device.deviceplatform.deviceplatformvendorname.deviceplatformvendor.vendor,
    pageview.device.deviceplatform.deviceplatformvendorname.name,
    pageview.device.deviceplatform.version,
    pageview.device.devicebrowser.devicebrowservendorname.devicebrowservendor.vendor,
    pageview.device.devicebrowser.devicebrowservendorname.name,
    pageview.device.devicebrowser.version,
    pageview.device.devicehardware.devicehardwarevendor.vendor,
    pageview.device.devicehardware.name,
    pageview.device.devicescreeninches,
    pageview.device.devicetype.type,
    pageview.page.name,
    pageview.pagegroup.name,
    pageview.url,
    pageview.rtprofile.name,
    pageview.rtvisit,
    pageview.rtvisitor,
    pageview.rtnewvisitor,
    pageview.rtnewvisitor2pg 
  }
};
