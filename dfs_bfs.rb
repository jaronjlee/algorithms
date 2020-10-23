def dfs(target)
        return self if self.value == target
        self.children.each do |child|
            memo = child.dfs(target)
            return memo unless memo.nil?
        end
        nil
    end

def bfs(target)
    queue = [self]
    until queue.empty?
        temp = queue.shift
        return temp if temp.value == target
        queue += temp.children
    end
    nil
end