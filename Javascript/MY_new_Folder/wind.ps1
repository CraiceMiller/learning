$name = "Craice"
$bool = $true


#just creating a function 
function print {
    param ($value)
    Write-Output $value
}

function binary ($array, $target){
    <#
    .SYNOPSIS
     This will just attempt to search the value at .It will return the index of the target
    
    .DESCRIPTION
    Long description 
    it will search throught ever value untill it found it, -1 otherwise
    
    .PARAMETER array
    Parameter description 
    his is the main array that the function will attempt to look into. 
    
    .PARAMETER target
    Parameter description 
    the value we want to search 
    
    .EXAMPLE
    An example 
    >>> binary -array @(1,2,3,4) -target 3 
        #output: 2

    
    .NOTES
    General notes
    this is my attempt to learn new lenaguages :3, today is Sempter 18th, 2025, at 19:00 hrs...
    #>
    $start = 0
    $end = $array.Count -1

    while ($start -le $end){
        $mid = ($start + $end) / 2
        if ($array[$mid] -eq $target){
            return $mid
        }
        elseif ($array[$mid] -le $target){
            $start = $mid + 1
        }else {
            $end = $mid -1
        }
    }

    return -1
}


print -value $name

for ($i = 0; $i -le 10; $i++){
    print -value $i
}

if ($bool){
    print -value "okay"
}else {
    print -value "No okay"
}


$nums = @(1,2,3,4,5,6,7,8,9,10)
$index = binary -array $nums -target 2

print -value $index
$nums.Insert(20,30)


for ($i = 0; $i -le $nums.Count; $i++){
    $element = $nums[$i]
    print -value $element
}



print -value $nums
print -value $nums.IsReadOnly