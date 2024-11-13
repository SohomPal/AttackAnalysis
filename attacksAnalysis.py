from itertools import combinations

AWS_REGIONS = {
    '16.170.36.145': 'eu-north-1',
    '35.181.178.104': 'eu-west-3',
    '43.204.44.211': 'ap-south-1',
    '52.57.58.5': 'eu-central-1',
    '52.215.196.41': 'eu-west-1',
    '47.130.38.124': 'ap-southeast-1',
    '18.181.8.135': 'ap-northeast-1',
    '35.155.161.107': 'us-west-2',
    '3.128.38.254': 'us-east-2',
    '15.222.98.16': 'ca-central-1',
    '54.219.111.3': 'us-west-1',
    '13.237.52.2': 'ap-southeast-2',
    '43.200.198.222': 'ap-northeast-2'

}

GCA_PREMIUM_REGIONS = {
    "34.75.246.52": "us-east1",
    "34.171.228.132": "us-central1",
    "34.83.63.223": "us-west1",
    "34.140.35.230": "europe-west1",
    "34.88.225.17": "europe-north1",
    "35.221.197.15": "asia-east1",
    "35.185.188.182": "asia-southeast1"
}

GCA_FREE_REGIONS = {
    "35.211.239.179": "us-east1",
    "35.209.87.57": "us-central1",
    "35.212.128.228": "us-west1",
    "35.210.226.98": "europe-west1",
    "35.217.9.53": "europe-north1",
    "35.206.237.180": "asia-east1",
    "35.213.170.66": "asia-southeast1"
}


def redefineVPs(results, type):
    if type == 'mpic':
        for pair in results:
            results[pair] = [AWS_REGIONS[ip] for ip in results[pair]]
    if type == 'gca-p':
        for pair in results:
            results[pair] = [GCA_PREMIUM_REGIONS[ip] for ip in results[pair]]
    if type == 'gca-f':
        for pair in results:
            results[pair] = [GCA_FREE_REGIONS[ip] for ip in results[pair]]

    return results


def calculate_resilience(results, N_Minus_Quorum, relevant_regions, type):
    if type == 'mpic':
        regions = AWS_REGIONS
    if type == 'gca-p':
        regions = GCA_PREMIUM_REGIONS
    if type == 'gca-f':
       regions = GCA_FREE_REGIONS

    relevant_regions = {regions[region] for region in relevant_regions}
    resilience_points = 0
    total_attacks = 0

    for pair in results:
        total_attacks += 1
        true_count = 0

        for perspective in results[pair]:
            if perspective in relevant_regions:
                true_count += 1

        # Check if attack succeeded based on 1 fail quorum policy
        if true_count < (len(relevant_regions) - N_Minus_Quorum):
            resilience_points += 1

    average_resilience = resilience_points / total_attacks
    return average_resilience


def bestDeployments(results, type, N_Minus_Quorum: int, perspectiveSize: int) -> list:
    if type == 'mpic':
        regions = AWS_REGIONS
    elif type == 'gca-f':
        regions = GCA_FREE_REGIONS
    elif type == 'gca-p':
        regions = GCA_PREMIUM_REGIONS

    all_combinations = list(combinations(regions, perspectiveSize))
    resilience_scores = []

    for combination in all_combinations:
        relevant_regions = {regions[region] for region in list(combination)}
        avg_resilience = calculate_resilience(results, N_Minus_Quorum, list(combination), type)
        resilience_scores.append((list(relevant_regions), avg_resilience))

    # Sort combinations by resilience value in descending order
    resilience_scores.sort(key=lambda x: x[1], reverse=True)

    # Return the top 10 combinations
    return resilience_scores[:10]