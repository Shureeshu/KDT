new tempusDominus.TempusDominus(document.getElementById('datetimepicker1'), {
  display: { 
      components: {
          seconds: false,
          useTwentyfourHour: false,
      },
      icons: {
          type: 'icons',
          time: 'fa fa-solid fa-clock',
          date: 'fa fa-solid fa-calendar',
          up: 'fa fa-solid fa-arrow-up',
          down: 'fa fa-solid fa-arrow-down',
          previous: 'fa fa-solid fa-chevron-left',
          next: 'fa fa-solid fa-chevron-right',
          today: 'fa fa-solid fa-calendar-check',
          clear: 'fa fa-solid fa-trash',
          close: 'fas fa-solid fa-xmark'
      },
  },
});