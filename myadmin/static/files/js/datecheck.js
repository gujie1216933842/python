/**
   * 计算两日期时间差
   * @param   interval 计算类型：D是按照天、H是按照小时、M是按照分钟、S是按照秒、T是按照毫秒
   * @param  date1 起始日期  格式为年月格式 为2012-06-20
   * @param  date2 结束日期
   * @return
   */
   function countTimeLength(interval, date1, date2) {
      var objInterval = {
         'D' : 1000 * 60 * 60 * 24,
         'H' : 1000 * 60 * 60,
         'M' : 1000 * 60,
         'S' : 1000,
         'T' : 1
      };
      interval = interval.toUpperCase();
      var dt1 = Date.parse(date1.replace(/-/g, "/"));
      var dt2 = Date.parse(date2.replace(/-/g, "/"));
      try {
         return ((dt2 - dt1) / objInterval[interval]);
      } catch (e) {
         return e.message;
      }
   }