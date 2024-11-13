import json
import attacksAnalysis as aa
import os


def list_json_files(folder_path = '/Users/sohompal/Documents/Open-MPIC_Experimental_Data/'):
    """
    Returns a list of all JSON file names in the specified folder.

    :param folder_path: Path to the folder containing JSON files.
    :return: List of JSON file names.
    """
    json_files = [file for file in os.listdir(folder_path) if file.endswith('.json')]
    return json_files

# json_files = list_json_files()

# for json in json_files:
#     mg.printMap(json)

#mg.printMap('amsterdam01-ufmg01-pres3.json')


def openFiles(ggp_file, ggf_file, om_file):
    with open(ggp_file, 'r') as file:
        ggp_data = json.load(file)
    with open(ggf_file, 'r') as file:
        ggf_data = json.load(file)
    with open(om_file, 'r') as file:
        om_data = json.load(file)

    return[ggp_data, ggf_data, om_data]


def formatData(files):
    data = []
    for jsonFile in files:
        attackDict = {}
        for attacker in jsonFile:
            for victim in jsonFile[attacker]:
                attackDict[(attacker, victim)] = jsonFile[attacker][victim]
        data.append(attackDict)
    return data


files = openFiles('ggp_ips.json', 'ggf_ips.json', 'om_ips.json')
ggp, ggf, om = formatData(files)

om = aa.redefineVPs(om, 'mpic')
ggf = aa.redefineVPs(ggf, 'gca-f')
ggp = aa.redefineVPs(ggp, 'gca-p')


# print('GCA-Free - Quorum of 6/7:', aa.calculate_resilience(ggf, 1, aa.GCA_FREE_REGIONS, 'gca-f'))
# print('GCA-Free - Quorum of 5/7:', aa.calculate_resilience(ggf, 2, aa.GCA_FREE_REGIONS, 'gca-f'))
# print('GCA-Premium - Quorum of 6/7:', aa.calculate_resilience(ggp, 1, aa.GCA_PREMIUM_REGIONS, 'gca-p'))
# print('GCA-Premium - Quorum of 5/7:', aa.calculate_resilience(ggp, 2, aa.GCA_PREMIUM_REGIONS, 'gca-p'))
# print('Open MPIC - Quorum of 10/13:', aa.calculate_resilience(om, 3, aa.AWS_REGIONS, 'mpic'))
# print('Open MPIC - Quorum of 12/13:', aa.calculate_resilience(om, 1, aa.AWS_REGIONS, 'mpic'))

print('Finding Best Sets from Each')

print('\nBEST GCA-Free Sets of 6, Quorum: N')
bestDeployments = aa.bestDeployments(ggf, 'gca-f', 0, 6)
for combination, resilience in bestDeployments:
    print(f"Combination: {combination}, Average Resilience: {resilience}")

print('\nBEST GCA-Free Sets of 6, Quorum: N-1')
bestDeployments = aa.bestDeployments(ggf, 'gca-f', 1, 6)
for combination, resilience in bestDeployments:
    print(f"Combination: {combination}, Average Resilience: {resilience}")

print('\nBEST GCA-Free Sets of 6, Quorum: N-2')
bestDeployments = aa.bestDeployments(ggf, 'gca-f', 2, 6)
for combination, resilience in bestDeployments:
    print(f"Combination: {combination}, Average Resilience: {resilience}")

print('\nBEST GCA-Premium Sets of 6, Quorum: N')
bestDeployments = aa.bestDeployments(ggp, 'gca-p', 0, 6)
for combination, resilience in bestDeployments:
    print(f"Combination: {combination}, Average Resilience: {resilience}")

print('\nBEST GCA-Premium Sets of 6, Quorum: N-1')
bestDeployments = aa.bestDeployments(ggp, 'gca-p', 1, 6)
for combination, resilience in bestDeployments:
    print(f"Combination: {combination}, Average Resilience: {resilience}")

print('\nBEST GCA-Premium Sets of 6, Quorum: N-2')
bestDeployments = aa.bestDeployments(ggp, 'gca-p', 2, 6)
for combination, resilience in bestDeployments:
    print(f"Combination: {combination}, Average Resilience: {resilience}")

print('\nBEST Open-MPIC Sets of 6, Quorum: N')
bestDeployments = aa.bestDeployments(om, 'mpic', 0, 6)
for combination, resilience in bestDeployments:
    print(f"Combination: {combination}, Average Resilience: {resilience}")

print('\nBEST Open-MPIC Sets of 6, Quorum: N-1')
bestDeployments = aa.bestDeployments(om, 'mpic', 1, 6)
for combination, resilience in bestDeployments:
    print(f"Combination: {combination}, Average Resilience: {resilience}")

print('\nBEST Open-MPIC Sets of 6, Quorum: N-2')
bestDeployments = aa.bestDeployments(om, 'mpic', 2, 6)
for combination, resilience in bestDeployments:
    print(f"Combination: {combination}, Average Resilience: {resilience}")

print('\nBEST GCA-Free Sets of 5, Quorum: N')
bestDeployments = aa.bestDeployments(ggf, 'gca-f', 0, 5)
for combination, resilience in bestDeployments:
    print(f"Combination: {combination}, Average Resilience: {resilience}")

print('\nBEST GCA-Free Sets of 5, Quorum: N-1')
bestDeployments = aa.bestDeployments(ggf, 'gca-f', 1, 5)
for combination, resilience in bestDeployments:
    print(f"Combination: {combination}, Average Resilience: {resilience}")

print('\nBEST GCA-Free Sets of 5, Quorum: N-2')
bestDeployments = aa.bestDeployments(ggf, 'gca-f', 2, 5)
for combination, resilience in bestDeployments:
    print(f"Combination: {combination}, Average Resilience: {resilience}")

print('\nBEST GCA-Premium Sets of 5, Quorum: N')
bestDeployments = aa.bestDeployments(ggp, 'gca-p', 0, 5)
for combination, resilience in bestDeployments:
    print(f"Combination: {combination}, Average Resilience: {resilience}")

print('\nBEST GCA-Premium Sets of 5, Quorum: N-1')
bestDeployments = aa.bestDeployments(ggp, 'gca-p', 1, 5)
for combination, resilience in bestDeployments:
    print(f"Combination: {combination}, Average Resilience: {resilience}")

print('\nBEST GCA-Premium Sets of 5, Quorum: N-2')
bestDeployments = aa.bestDeployments(ggp, 'gca-p', 2, 5)
for combination, resilience in bestDeployments:
    print(f"Combination: {combination}, Average Resilience: {resilience}")

print('\nBEST Open-MPIC Sets of 5, Quorum: N')
bestDeployments = aa.bestDeployments(om, 'mpic', 0, 5)
for combination, resilience in bestDeployments:
    print(f"Combination: {combination}, Average Resilience: {resilience}")

print('\nBEST Open-MPIC Sets of 5, Quorum: N-1')
bestDeployments = aa.bestDeployments(om, 'mpic', 1, 5)
for combination, resilience in bestDeployments:
    print(f"Combination: {combination}, Average Resilience: {resilience}")

print('\nBEST Open-MPIC Sets of 5, Quorum: N-2')
bestDeployments = aa.bestDeployments(om, 'mpic', 2, 5)
for combination, resilience in bestDeployments:
    print(f"Combination: {combination}, Average Resilience: {resilience}")

# print('LetsEncrypt Base Resilience:', rc.LE_ResCalc(json_files), '\n')
# print('LetsEncrypt Resilience With Additional Vantage Point:')
# resilienceMap = rc.LE_PlusOne_ResCalc(json_files)
# for key, value in resilienceMap.items():
#     print(f"{key}: {value}")

# print('\nLetsEncrypt Enhanced Resilience:', rc.LE_EnhancedResCalc(json_files), '\n')
#
# print('\nLetsEncrypt Enhanced Resilience With Best Additional Vantage Point:')
# enhancedResilienceMap = rc.LE_PlusOne_EnhancedResCalc(json_files)
# for key, value in enhancedResilienceMap.items():
#     print(f"{key}: {value}")
#
# print('\nBest Open-MPIC Deployments (4 Perspective): ')
# bestdeployments = rc.bestDeployment(json_files, 4)
# for combination, resilience in bestdeployments:
#     print(f"Combination: {combination}, Average Resilience: {resilience}")
#
# print('\nBest Open-MPIC Deployments (5 Perspective): ')
# bestdeployments = rc.bestDeployment(json_files, 5)
# for combination, resilience in bestdeployments:
#     print(f"Combination: {combination}, Average Resilience: {resilience}")
#
# print('\nBest Open-MPIC Deployments (6 Perspective): ')
# bestdeployments = rc.bestDeployment(json_files, 6)
# for combination, resilience in bestdeployments:
#     print(f"Combination: {combination}, Average Resilience: {resilience}")
#
# print('\nBest Open-MPIC Enhanced Deployments (4 Perspective): ')
# bestdeployments = rc.bestDeploymentEnhanced(json_files, 4)
# for combination, resilience in bestdeployments:
#     print(f"Combination: {combination}, Average Resilience: {resilience}")
#
# print('\nBest Open-MPIC Enhanced Deployments (5 Perspective): ')
# bestdeployments = rc.bestDeploymentEnhanced(json_files, 4)
# for combination, resilience in bestdeployments:
#     print(f"Combination: {combination}, Average Resilience: {resilience}")