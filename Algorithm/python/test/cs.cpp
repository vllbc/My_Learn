#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
long long max_yue(long long a,long long b){
	return (b==0) ? a : max_yue(b,a%b);
}
long long a_b(long long a,long long b){
	if(a == b){
		return a;
	}
	if (b < a){
		swap(a,b);
	}
	return a_b(min(b/a,a),max(b/a,a)); 
}
int main(){
	int n;
	cin >> n;
	vector<long long> nums;
	for(int i = 0;i<n;i++){
		long long a;
		cin >> a;
		nums.push_back(a);
	}
	sort(nums.begin(),nums.end());
	vector<long long> fenzi;
	vector<long long> fenmu;
	for(int i = 0;i<nums.size()-1;i++){
		if(nums[i] == nums[i+1])
			continue;      
		long long y = max_yue(nums[i],nums[i+1]);
		fenzi.push_back(nums[i+1]/y);
		fenmu.push_back(nums[i]/y);
	}

	long long fz = fenzi[0];
	long long fm = fenmu[0];
	for(int i = 1;i<fenzi.size();i++){
		fz = a_b(fz,fenzi[i]);
		fm = a_b(fm,fenmu[i]);
	} 
	cout << fz << "/" << fm << endl;
	return 0;
}
