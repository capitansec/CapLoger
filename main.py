from controllers import counterArray

class LogAnalysis:
    def __init__(self,log_path):
        self.log_path = log_path # log file abs location

    def __str__(self):
        return f"Active log file => {self.log_path}"      # Default method for print log file name

    def readFile(self):
        ipList = [] # all source ips
        uniqueIps = [] # unique source ips
        f = open(self.log_path, 'r').readlines()
        for line in f: # single loop for bigO
            sourceIp = line.split(",")[0] # parse for get ip
            ipList.append(sourceIp)

            if sourceIp not in uniqueIps:
                try:
                    int(sourceIp.split(".")[0]) # try to prevent appending non ip elements to uniques !
                    uniqueIps.append(sourceIp)
                except ValueError:
                    continue
        return ipList, uniqueIps

    def sourceCounts(self):
        counterArray(self.readFile()[0], self.readFile()[1])


log = LogAnalysis("web_log.txt")

log.sourceCounts()