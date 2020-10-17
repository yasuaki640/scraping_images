script_tags = ['''<script type="text/javascript">
        (function() {
  var docElement = document.documentElement;
  var classRE = new RegExp('(^|\\s)no-js(\\s|$)');
  var className = docElement.className;
  docElement.className = className.replace(classRE, '$1js$2');
})();
</script>''', '''<script type="text/javascript">
(function() {
  if ('PerformanceObserver' in window && 'PerformancePaintTiming' in window) {
    window.__bufferedPerformance = [];
    var ob = new PerformanceObserver(function(e) {
      window.__bufferedPerformance.push.apply(window.__bufferedPerformance,e.getEntries());
    });
    ob.observe({entryTypes:['paint']});
  }

  window.__bufferedErrors = [];
  window.onerror = function(message, url, line, column, error) {
    window.__bufferedErrors.push({
      message: message,
      url: url,
      line: line,
      column: column,
      error: error
    });
    return false;
  };
  window.__initialData = {
    pending: true,
    waiting: []
  };
  function asyncFetchSharedData(extra) {
    var sharedDataReq = new XMLHttpRequest();
    sharedDataReq.onreadystatechange = function() {
          if (sharedDataReq.readyState === 4) {
            if(sharedDataReq.status === 200){
              var sharedData = JSON.parse(sharedDataReq.responseText);
              window.__initialDataLoaded(sharedData, extra);
            }
          }
        }
    sharedDataReq.open('GET', '/data/shared_data/', true);
    sharedDataReq.send(null);
  }
  function notifyLoaded(item, data) {
    item.pending = false;
    item.data = data;
    for (var i = 0;i < item.waiting.length; ++i) {
      item.waiting[i].resolve(item.data);
    }
    item.waiting = [];
  }
  function notifyError(item, msg) {
    item.pending = false;
    item.error = new Error(msg);
    for (var i = 0;i < item.waiting.length; ++i) {
      item.waiting[i].reject(item.error);
    }
    item.waiting = [];
  }
  window.__initialDataLoaded = function(initialData, extraData) {
    if (extraData) {
      for (var key in extraData) {
        initialData[key] = extraData[key];
      }
    }
    notifyLoaded(window.__initialData, initialData);
  };
  window.__initialDataError = function(msg) {
    notifyError(window.__initialData, msg);
  };
  window.__additionalData = {};
  window.__pendingAdditionalData = function(paths) {
    for (var i = 0;i < paths.length; ++i) {
      window.__additionalData[paths[i]] = {
        pending: true,
        waiting: []
      };
    }
  };
  window.__additionalDataLoaded = function(path, data) {
    if (path in window.__additionalData) {
      notifyLoaded(window.__additionalData[path], data);
    } else {
      console.error('Unexpected additional data loaded "' + path + '"');
    }
  };
  window.__additionalDataError = function(path, msg) {
    if (path in window.__additionalData) {
      notifyError(window.__additionalData[path], msg);
    } else {
      console.error('Unexpected additional data encountered an error "' + path + '": ' + msg);
    }
  };
  
})();
</script>''', '''<script type="text/javascript">

/*
 Copyright 2018 Google Inc. All Rights Reserved.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
*/

(function(){function g(a,c){b||(b=a,f=c,h.forEach(function(a){removeEventListener(a,l,e)}),m())}function m(){b&&f&&0<d.length&&(d.forEach(function(a){a(b,f)}),d=[])}function n(a,c){function k(){g(a,c);d()}function b(){d()}function d(){removeEventListener("pointerup",k,e);removeEventListener("pointercancel",b,e)}addEventListener("pointerup",k,e);addEventListener("pointercancel",b,e)}function l(a){if(a.cancelable){var c=performance.now(),b=a.timeStamp;b>c&&(c=+new Date);c-=b;"pointerdown"==a.type?n(c,
a):g(c,a)}}var e={passive:!0,capture:!0},h=["click","mousedown","keydown","touchstart","pointerdown"],b,f,d=[];h.forEach(function(a){addEventListener(a,l,e)});window.perfMetrics=window.perfMetrics||{};window.perfMetrics.onFirstInputDelay=function(a){d.push(a);m()}})();
</script>''']
