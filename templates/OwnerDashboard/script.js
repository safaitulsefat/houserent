
  var subjectObject = {
    "Dhaka": {
      "Dhaka": ["mirpur10", "Gulsan", "Agargaw", "Motizil", "Bosundara"]
    },
    "Chittagong": {
      "Chittagong": ["Andorkilla", "New market", "Chawbazar", "Kulshi"],
    }
  };

  window.onload = function() {
    var sellLandForm = document.getElementById("sell-land-form");
    var sellFlatForm = document.getElementById("sell-flat-form");

    if (sellLandForm) {
      var subjectSel = sellLandForm.querySelector("#division");
      var topicSel = sellLandForm.querySelector("#district");
      var chapterSel = sellLandForm.querySelector("#location");
    }

    if (sellFlatForm) {
      var subjectSel = sellFlatForm.querySelector("#divission");
      var topicSel = sellFlatForm.querySelector("#district");
      var chapterSel = sellFlatForm.querySelector("#location");
    }

    for (var x in subjectObject) {
      subjectSel.options[subjectSel.options.length] = new Option(x, x);
    }

    subjectSel.onchange = function() {
      chapterSel.length = 1;
      topicSel.length = 1;

      for (var y in subjectObject[this.value]) {
        topicSel.options[topicSel.options.length] = new Option(y, y);
      }
    }

    topicSel.onchange = function() {
      chapterSel.length = 1;

      var z = subjectObject[subjectSel.value][this.value];
      for (var i = 0; i < z.length; i++) {
        chapterSel.options[chapterSel.options.length] = new Option(z[i], z[i]);
      }
    }
  }


